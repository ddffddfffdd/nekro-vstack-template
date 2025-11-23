# Nekro VStack Template ⚡️

> **专为 AI 辅助编程设计的全栈开发模板 · 垂直切分架构 · MacOS 风格 UI**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![TypeScript](https://img.shields.io/badge/typescript-5.6+-3178C6.svg?logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg?logo=react&logoColor=white)](https://react.dev)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com)

---

**Nekro VStack** 是一个旨在最大化 **LLM (大语言模型)** 代码理解与生成效率的现代全栈开发脚手架。它打破了传统的前后端分离代码组织方式，采用 **垂直切分架构 (Vertical Slice Architecture)**，将同一功能的 "前端 UI" 与 "后端逻辑" 物理聚合，显著降低了 AI 上下文检索的开销，让 Feature 开发如搭积木般高效。

## ✨ 核心亮点

### 🧠 AI Native 架构

- **垂直切分 (Vertical Slicing)**: 前后端代码按功能聚合在 `src/features/[feature_name]` 下，AI 一次检索即可获取完整上下文。
- **类型对齐**: 后端 Pydantic 模型与前端 TypeScript 类型通过工具链自动同步，减少幻觉。

### 🎨 极致 UI/UX

- **MacOS 风格**: 深度定制的 MUI v6 主题，内置玻璃拟态 (Glassmorphism)、Inter 字体。
- **流畅动画**: 集成 Framer Motion，预设平滑的页面过渡和列表交错动画。
- **自适应主题**: 完美支持 Light/Dark 模式无缝切换。

### 🛠 现代技术栈

- **后端**: FastAPI (Async), Tortoise-ORM, Pydantic v2, uv (极速包管理), SSE 实时推送。
- **前端**: React 18, React Router v7, Zustand, Vite, Axios。
- **工程化**: Docker 容器化, GitHub Actions CI/CD, Windows 原生应用打包支持。

---

## 🚀 快速开始

### 1. 初始化

```bash
# 初始化环境 (检查依赖、生成配置)
./scripts/init-project.sh
```

### 2. 启动开发

```bash
# 启动所有服务 (前端 + 后端)
pnpm dev:all

# 或者分别启动
# pnpm dev:backend
# pnpm dev:frontend
```

### 3. 访问应用

- **Web UI**: `http://localhost:5173`
- **API Docs**: `http://localhost:9871/docs`
- **默认账号**: `admin` / `admin`

详细说明：[快速开始指南](./docs/getting-started.md)

---

## 📁 架构概览

```text
src/
├── features/          # 🧩 垂直功能切片 (AI 关注重点)
│   └── [feature]/
│       ├── frontend/  # UI 组件 + API Hooks + 状态
│       └── backend/   # API 路由 + DB 模型 + Schemas
├── backend/           # ⚙️ 后端核心 (Auth, Logging, Config)
└── frontend/          # 🖥️ 前端基建 (Router, Theme, Utils)
```

详细架构说明请参阅 [架构文档](./docs/architecture.md)。

---

## 📚 文档中心

- **[开发指南](./docs/development.md)**: 如何创建一个新 Feature（核心阅读）
- **[部署指南](./docs/deployment.md)**: Docker 与 Windows 部署
- **[AI 协作规范](./.cursor/rules/global.mdc)**: Cursor/Copilot 最佳实践
- **[命令参考](./docs/commands.md)**: 常用命令速查

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！提交前请确保通过类型检查与 Lint：

```bash
pnpm type-check
pnpm lint:backend
```

## 📄 License

MIT © Nekro VStack
