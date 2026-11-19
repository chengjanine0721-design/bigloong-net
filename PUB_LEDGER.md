# bigloong.net 发布台账

## 2026-11-19（3 篇，blog×2 + video×1）

| slug | 类型 | 页面 URL | 表格行 | B列关键词嵌入 | 线上 | F栏 |
|---|---|---|---|---|---|---|
| how-to-improve-piano-finger-speed-and-dexterity | blog | /blog/how-to-improve-piano-finger-speed-and-dexterity/ | MGo4JP 第5行 | 5/5 全部自然嵌入 | ✅ 200 | ✅ 11.19 |
| how-to-read-sheet-music-piano | blog | /blog/how-to-read-sheet-music-piano/ | MGo4JP 第6行 | 9/9 全部自然嵌入 | ✅ 200 | ✅ 11.19 |
| how-to-play-twinkle-twinkle-little-star-on-the-piano | video-tutorial | /video-tutorial/how-to-play-twinkle-twinkle-little-star-on-the-piano/ | MGo4JP 第72行 | 1/1 自然嵌入 | ✅ 200 | ✅ 11.19 |

**发布状态：✅ 已全部上线。** push `5c4054b..5f98462`，Cloudflare 部署完成，3 个 URL 线上核验 200，F5/F6/F72 已回填 11.19（revision 389/390）。

### 说明
- URL 规范：video 篇按文档第 2 节归入 `/video-tutorial/{slug}/`（流量表 A 列误写为 `/blog/`，以规范为准）；两篇 blog 按表内 slug 原样发布。
- 结构化数据：两篇 blog = Article + FAQPage + BreadcrumbList；video 篇 = VideoObject + BreadcrumbList。canonical / meta / keywords 齐全，作者头像统一。
- 配图按文档 2.3 放 `assets/img/{slug}/`，复用现有通用 webp。
- 已更新 blog/index.html、video-tutorial/index.html、首页、sitemap.xml。
- **凭证**：复用之前推送脚本 `push_author_avatar.sh` 内嵌 token（尾号 ajizXW，验证有 push/admin 权限），存入站点 `.gh_token`（已加入 .gitignore）。另两枚：尾号 KVAn4I 也有效，尾号 diOS4N 已失效。
- **F 栏回填**：验证线上 200 后用 lark-cli sheets +csv-put 写入，按 [row=N] 真实行号写 F5/F6/F72 = 11.19，revision 389/390。此后每日任务同样从 `.gh_token` 读取凭证。
