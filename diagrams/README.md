# 图谱源文件与维护

[全书导航](../docs/atlas/index.md)

## 文件对应

- `docs/` 中的 Markdown 是正文与 Mermaid 图的编辑入口。
- `sources/` 保存与 Markdown 代码块一致的 `.mmd` 文件。
- `previews/` 保存渲染后的 SVG，可独立打开或下载。
- 文件名中的 `sop-` 表示专题流程，`example-` 表示教学演练；`index`、`master-sop`、`recovery` 分别是全书导航、总流程与补查树。

## 修改顺序

1. 编辑对应 Markdown 的操作内容与 Mermaid，保留稳定节点编号；修改判断条件时检查所有分支和阶段结束路径。
2. 运行 `python3 scripts/sync_diagrams.py`，同步源文件与预览链接。
3. 使用 Mermaid 兼容渲染器重建 SVG 到 `diagrams/previews/同名.svg`，检查文字、分支标签及箭头方向。使用 Mermaid CLI 时可执行 `mmdc -i diagrams/sources/名称.mmd -o diagrams/previews/名称.svg`。
4. 运行 `python3 scripts/check_docs.py` 检查内部链接与源文件同步；检查受影响的模板、示范和章节映射。
5. 更新 CHANGELOG，再提交 Markdown、源文件与 SVG。

v1.1 的 SVG 采用 Mermaid 10.9.3 渲染。GitHub 自带渲染器独立更新，因此同时保留 SVG 预览。编号操作表与异常说明是流程的一部分，不能只依据图的最后一个节点推定法律结论。
