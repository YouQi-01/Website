# YouQi-01 个人博客

[y.ioft.dpdns.org](https://y.ioft.dpdns.org/)

## 项目概述

YouQi-01 是一个简洁高效的个人博客系统，基于静态HTML/CSS/JavaScript构建，无需数据库支持。

## 功能特性

- 📝 文章发布与管理
- 🏷️ 文章分类与标签
- 🔍 文章归档与搜索
- ✨ 响应式设计，适配各种设备
- 🌙 即将支持暗黑模式
- ⚡ 快速加载，优化性能

## 快速开始

1. 克隆项目到本地：
   ```bash
   git clone https://github.com/your-repo/website.git
   ```

2. 添加新文章：
   - 在`docs/`目录下创建Markdown文件
   - 在`docs/docs.json`中添加文章元数据

3. 本地预览：
   - 使用Live Server等工具打开`index.html`

## 开发指南

### 技术栈

- 前端：HTML5, CSS3, JavaScript
- Markdown解析：marked.js
- 部署：静态网站托管

### 项目结构

```
├── index.html        # 首页/文章页
├── archive.html      # 文章归档
├── 404.html          # 404页面
├── docs/             # 文章目录
│   ├── docs.json     # 文章元数据
│   └── *.md          # Markdown文章
└── ReadMe.md         # 项目文档
```

## 未来计划

- [ ] 添加暗黑模式支持
- [ ] 实现全文搜索功能
- [ ] 优化移动端体验

## 许可证

MIT License