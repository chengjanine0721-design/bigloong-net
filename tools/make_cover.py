# -*- coding: utf-8 -*-
"""
Blog 封面图生成器 —— 两步分层的第 2 步：在纯视觉底图上叠加真实文字节点。

规范：(1200x800, <200KB, JPEG q90 subsampling=4:4:4 progressive)
  - 左侧深色渐变遮罩保证文字对比度
  - 信息层级: 眉标 -> 主标题(2行) -> 副标题 -> 署名 -> 品牌
  - 字体: 主标题 Playfair Display Bold / 眉标署名 Outfit Medium / 副标题 Lora Regular

用法:
  python make_cover.py --base <底图路径> --out <输出路径> \
      --eyebrow "BEGINNER GUIDE / 15 QUICK TIPS" \
      --title "How to Start Learning Piano" \
      --subtitle "Everything you need to know to play your first song." \
      --author "Alice Baker" --read "18 MIN READ"

底图要求: AI 生成, prompt 末尾必须是 "no text, no words, no letters";
主体偏右, 左侧留暗部负空间。若底图带水印, 先用 --inpaint 区域擦除再生成。
"""
import argparse
import os
import io
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 800
LEFT = 76
GOLD = (232, 184, 75)
WHITE = (255, 255, 255)
CREAM = (232, 226, 216)

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts")
F_PLAYFAIR = os.path.join(FONT_DIR, "PlayfairDisplay-Bold.ttf")
F_OUTFIT = os.path.join(FONT_DIR, "Outfit-Medium.ttf")
F_LORA = os.path.join(FONT_DIR, "Lora-Regular.ttf")


def load_font(path, size, weight=None):
    """加载字体; 可变字体按需设置 wght 轴。"""
    f = ImageFont.truetype(path, size)
    try:
        names = [n.decode() if isinstance(n, bytes) else n for n in f.get_variation_names()]
        if weight:
            target = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold"}.get(weight)
            if target and target in names:
                f.set_variation_by_name(target)
            else:
                # 直接设轴: Playfair/Outfit/Lora 的 wght 轴索引 0
                axes = [a.axis for a in f.get_variation_axes()]
                if "wght" in [a.decode() if isinstance(a, bytes) else a for a in axes]:
                    f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def draw_spaced(draw, xy, text, font, fill, spacing=2):
    """逐字符绘制并加字距(眉标/署名用)。"""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        box = draw.textbbox((0, 0), ch, font=font)
        x += (box[2] - box[0]) + spacing
    return x


def wrap_lines(draw, text, font, max_width, max_lines=2):
    """按像素宽度折行; 尽量在 max_lines 内放下全部词, 实在放不下才省略。"""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    # 超出 max_lines: 把前 N-1 行保留, 最后一行合并剩余词再截断加 …
    if len(lines) > max_lines:
        head = lines[:max_lines - 1]
        rest = " ".join(lines[max_lines - 1:])
        while draw.textlength(rest + "…", font=font) > max_width and rest:
            rest = rest[:-1]
        lines = head + [rest.rstrip() + "…"]
    return lines[:max_lines]


def gradient_overlay(base, light=False):
    """从左到右渐变遮罩: 左侧不透明, ~62% 处归零。
    默认深色遮罩(配白字); light=True 时用浅色遮罩(配深色字), 适配浅色底图。"""
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = ov.load()
    gx = 0.62 * W
    tint = (255, 252, 248) if light else (0, 0, 0)
    for x in range(W):
        t = max(0.0, 1.0 - x / gx)
        a = int(235 * (t ** 1.35)) + 26
        a = min(a, 245)
        for y in range(H):
            px[x, y] = tint + (a,)
    return Image.alpha_composite(base.convert("RGBA"), ov)


def inpaint_region(img, box):
    """用周围像素的模糊副本填充水印区域(简单 inpaint)。box=(l,t,r,b)。"""
    work = img.convert("RGB")
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rectangle(box, fill=255)
    blurred = work.filter(ImageFilter.GaussianBlur(28))
    work.paste(blurred, (0, 0), mask)
    return work


def build(args):
    # 1) 底图 -> 1200x800 中心裁剪填满
    base = Image.open(args.base).convert("RGB")
    bw, bh = base.size
    scale = max(W / bw, H / bh)
    nw, nh = int(bw * scale + 0.5), int(bh * scale + 0.5)
    base = base.resize((nw, nh), Image.LANCZOS)
    l, t = (nw - W) // 2, (nh - H) // 2
    base = base.crop((l, t, l + W, t + H))

    # 2) 可选: 擦水印
    if args.inpaint:
        box = tuple(int(v) for v in args.inpaint.split(","))
        base = inpaint_region(base, box)

    # 3) 渐变遮罩 (light 模式用浅色遮罩配深色字)
    light = getattr(args, "light", False)
    img = gradient_overlay(base, light=light)
    draw = ImageDraw.Draw(img)

    # 配色: 深色底图用白字+亮金; 浅色底图用深墨蓝字+深金
    if light:
        C_TITLE = (30, 32, 74)
        C_EYEBROW = (150, 104, 22)   # 深金, 浅底上可读
        C_SUB = (60, 64, 92)
        C_SIGN = (30, 32, 74)
        C_READ = (150, 104, 22)
        C_BRAND = (150, 104, 22)
        C_RULE = (150, 152, 168)
    else:
        C_TITLE = WHITE
        C_EYEBROW = GOLD
        C_SUB = CREAM
        C_SIGN = WHITE
        C_READ = GOLD
        C_BRAND = GOLD
        C_RULE = (120, 116, 108)

    # 4) 字体
    f_eyebrow = load_font(F_OUTFIT, 24, 500)
    f_title = load_font(F_PLAYFAIR, 82, 700)
    f_title_sm = load_font(F_PLAYFAIR, 70, 700)
    f_sub = load_font(F_LORA, 27, 400)
    f_sign = load_font(F_OUTFIT, 22, 500)
    f_read = load_font(F_OUTFIT, 18, 500)
    f_brand = load_font(F_OUTFIT, 20, 500)

    maxw = int(W * 0.42)  # 左侧文字区 ~40%

    # 5) 眉标(金色, 字距)
    eyebrow = args.eyebrow.upper()
    draw_spaced(draw, (LEFT, 132), eyebrow, f_eyebrow, C_EYEBROW, spacing=3)

    # 6) 金色短线
    draw.rounded_rectangle([LEFT, 182, LEFT + 58, 185], radius=1, fill=C_EYEBROW)

    # 7) 主标题(最多2行, 字号自适应: 大字号放不下完整标题则降级, 不截断)
    title = args.title
    title_sizes = [82, 76, 70, 64, 58]
    font, lines = None, None
    for sz in title_sizes:
        f = load_font(F_PLAYFAIR, sz, 700)
        ls = wrap_lines(draw, title, f, maxw + 60, 2)
        # 完整放下(无省略号)才采用
        if not any(ln.endswith("…") for ln in ls):
            font, lines = f, ls
            break
    if font is None:  # 极端长标题: 用最小字号, 接受省略
        font = load_font(F_PLAYFAIR, title_sizes[-1], 700)
        lines = wrap_lines(draw, title, font, maxw + 60, 2)
    ty = 214
    line_h = int(font.size * 1.12)
    for ln in lines:
        draw.text((LEFT, ty), ln, font=font, fill=C_TITLE, stroke_width=0)
        ty += line_h

    # 8) 副标题(最多2行)
    if args.subtitle:
        sub_y = ty + 14
        for ln in wrap_lines(draw, args.subtitle, f_sub, maxw - 10, 2):
            draw.text((LEFT, sub_y), ln, font=f_sub, fill=C_SUB)
            sub_y += 38

    # 9) 署名区(底部): 细线 + By <author> + 阅读时长
    draw.line([LEFT, 690, LEFT + 360, 690], fill=C_RULE, width=1)
    draw_spaced(draw, (LEFT, 706), "By " + args.author, f_sign, C_SIGN, spacing=1)
    if args.read:
        draw_spaced(draw, (LEFT, 738), args.read.upper(), f_read, C_READ, spacing=3)

    # 10) 品牌(右下)
    bw_brand = draw.textlength("bigloong.net", font=f_brand)
    draw.text((W - LEFT - bw_brand, H - 70), "bigloong.net", font=f_brand, fill=C_BRAND)

    out = img.convert("RGB")

    # 11) 压缩: q90 / 4:4:4 / progressive, 超 200KB 则逐档降 quality
    data = None
    quality = 90
    for q in range(90, 69, -2):
        buf = io.BytesIO()
        out.save(buf, format="JPEG", quality=q, subsampling=0, progressive=True, optimize=True)
        data = buf.getvalue()
        quality = q
        if len(data) < 200 * 1024:
            break

    with open(args.out, "wb") as fh:
        fh.write(data)

    # 12) 校验
    chk = Image.open(io.BytesIO(data))
    size_ok = chk.size == (W, H)
    bytes_ok = len(data) < 200 * 1024
    print("[make_cover] out=%s" % args.out)
    print("[make_cover] size=%s  bytes=%d (%.1f KB)  quality=%d  subsampling=4:4:4  progressive=yes"
          % (chk.size, len(data), len(data) / 1024, quality))
    print("[make_cover] size_ok=%s bytes_ok=%s  %s"
          % (size_ok, bytes_ok, "PASS" if (size_ok and bytes_ok) else "FAIL"))
    return 0 if (size_ok and bytes_ok) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="纯视觉底图路径(无文字)")
    ap.add_argument("--out", required=True, help="输出封面图路径")
    ap.add_argument("--eyebrow", default="BEGINNER GUIDE")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--author", default="Alice Baker")
    ap.add_argument("--read", default="")
    ap.add_argument("--inpaint", default="", help="水印区域 l,t,r,b, 如 1080,20,1190,70")
    ap.add_argument("--light", action="store_true", help="浅色底图模式: 浅色遮罩+深色字")
    args = ap.parse_args()
    raise SystemExit(build(args))


if __name__ == "__main__":
    main()
