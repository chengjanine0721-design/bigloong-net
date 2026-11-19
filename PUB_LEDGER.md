# bigloong.net 发布台账

## 2026-11-19（3 篇，blog×2 + video×1）

| slug | 类型 | 页面 URL | 表格行 | B列关键词嵌入 | 本地状态 | 线上 | F栏 |
|---|---|---|---|---|---|---|---|
| how-to-improve-piano-finger-speed-and-dexterity | blog | /blog/how-to-improve-piano-finger-speed-and-dexterity/ | MGo4JP 第5行 | 5/5 全部自然嵌入 | 已生成+本地提交 bbaa451 | 待 push | 待回填 11.19 |
| how-to-read-sheet-music-piano | blog | /blog/how-to-read-sheet-music-piano/ | MGo4JP 第6行 | 9/9 全部自然嵌入 | 已生成+本地提交 bbaa451 | 待 push | 待回填 11.19 |
| how-to-play-twinkle-twinkle-little-star-on-the-piano | video-tutorial | /video-tutorial/how-to-play-twinkle-twinkle-little-star-on-the-piano/ | MGo4JP 第72行 | 1/1 自然嵌入 | 已生成+本地提交 bbaa451 | 待 push | 待回填 11.19 |

### 说明
- URL 规范：video 篇按文档第 2 节归入 `/video-tutorial/{slug}/`（流量表 A 列误写为 `/blog/`，以规范为准）；两篇 blog 按表内 slug 原样发布。
- 结构化数据：两篇 blog = Article + FAQPage + BreadcrumbList；video 篇 = VideoObject + BreadcrumbList。canonical / meta / keywords 齐全，作者头像统一。
- 配图按文档 2.3 放 `assets/img/{slug}/`，复用现有通用 webp。
- 已更新 blog/index.html、video-tutorial/index.html、首页、sitemap.xml。
- **卡点**：本机无可用 GitHub PAT（环境变量 / .gh_token / git credential / git remote 全空），无法 push。本地 commit 已就绪（基于线上 5c4054b，快进无冲突），token 到位后 `git remote add origin https://<PAT>@github.com/chengjanine0721-design/bigloong-net.git && git push origin main` 即可。
- **F 栏回填**：SOP 要求验证线上 200 后再填，故 push 前不填，避免假记录。回填时用 lark-cli sheets +csv-put，按 [row=N] 真实行号写 F5/F6/F72 = 11.19。
