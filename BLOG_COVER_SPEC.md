# Blog 封面图生成规范（每日发布默认执行）

> 每篇新发布的 blog 都必须配一张封面图，站点的 `build.py` 中该篇 `cover_img` 字段指向它。
> 本规范固化于 2026-11-19。执行工具：`tools/make_cover.py`。

## 一、任务
根据文章内容生成一张英文 blog 封面图，尺寸 **1200×800**。

## 二、核心策略（关键）——两步分层
不要整图交给 AI 一次性生成（AI 直接渲染文字不可靠）。分两步：
1. **AI 只生成纯视觉底图**：prompt 末尾必须写 `no text, no words, no letters`，主体偏右、左侧留暗部负空间。
2. **本地叠加真实文字节点**：用 `tools/make_cover.py` 在底图上排版标题等文字，保证 100% 清晰、可编辑。

## 三、底图 prompt 要点
- 主题：从文章核心内容提炼（如钢琴初学者指南 / 文章 URL 主题）
- 风格：`editorial magazine photography, cinematic, premium, moody`
- 构图：主体偏右，左侧大面积暗部负空间供放标题
- 配色：`deep charcoal / near-black + warm brass gold highlights`
- 明确排除：`no text, no words, no letters, no watermark`

## 四、版式规范（脚本已实现）
- 左对齐非对称布局，左侧文字区约占 40%（脚本用 42%+自适应）
- 文字区叠加从左到右的深色渐变遮罩，保证对比度
- 信息层级：眉标(分类/技巧数) → 主标题(2行,字号自适应不截断) → 副标题 → 署名 → 品牌(bigloong.net)
- 金色细线/分隔线做点缀，统一强调色 `#E8B84B`

## 五、字体（已下载到 `assets/fonts/`）
- 主标题：Playfair Display Bold（可变字体，脚本设 wght=700）
- 眉标/署名：Outfit Medium（wght=500）
- 副标题：Lora Regular（wght=400）

## 六、技术参数（脚本自动保证并校验）
- 尺寸：1200×800（精确）
- 体积：**< 200 KB**
- 格式：JPEG，`quality=90 / subsampling=0(4:4:4) / progressive=True / optimize=True`；超 200KB 时自动逐档降 quality
- 不用 PNG（量化到最低仍超重）

## 七、质量把控
- 生图模型若强制打水印：用脚本 `--inpaint l,t,r,b` 擦除指定区域后再交付
- 交付前校验：脚本输出会打印 `size_ok` / `bytes_ok`，必须都是 True；并人工目检文字清晰、无水印、无压缩痕迹

## 八、标准执行命令

```bash
# 1) 用 ImageGen 生成纯视觉底图(prompt 末尾 no text, no words, no letters)，
#    保存到 assets/img/{slug}/base.jpg
#    ImageGen 会消耗积分(约 5-10/张)，属正常成本。

# 2) 叠加文字生成封面图
"C:/Users/14248/.workbuddy/binaries/python/envs/default/Scripts/python.exe" \
  "D:/workbuddy/buddy-files/bigloong-site/tools/make_cover.py" \
  --base  "D:/workbuddy/buddy-files/bigloong-site/assets/img/{slug}/base.jpg" \
  --out   "D:/workbuddy/buddy-files/bigloong-site/assets/img/{slug}/cover.jpg" \
  --eyebrow "BEGINNER GUIDE / 15 QUICK TIPS" \
  --title   "文章主标题" \
  --subtitle "一句副标题" \
  --author "Alice Baker" --read "18 MIN READ"

# 3) 校验输出: size=(1200,800) bytes<200KB quality<=90 且 size_ok=True bytes_ok=True
```

## 九、与站点生成的衔接
- 封面图产出后，在 `build.py` 的该 POSTS 条目加 `"cover_img": "/assets/img/{slug}/cover.jpg"`（同时把 `image` 也设为它）。
- 运行 `build.py` 重建：`build_article()` 会把 cover 渲染到右侧栏顶部，并自动写入 `og:image` 与结构化数据 `image`。
- 底图 `base.jpg` 可不入库（体积大），但保留便于复现；入库前确认 `.gitignore` 规则。
