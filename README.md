# Nekro VStack

**垂直切分的 AI 友好全栈开发模板**

Vertical-Split Full-Stack Template for AI-Powered Development

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![TypeScript](https://img.shields.io/badge/typescript-5.6+-blue.svg)](https://www.typescriptlang.org)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com)
[![Windows](https://img.shields.io/badge/windows-native-blue.svg)](https://microsoft.com)

---

## ✨ 核心特性

- **🏗️ 功能垂直切分** - 前后端代码按功能聚合，优化 AI 理解和检索效率
- **🔄 类型自动同步** - 后端 OpenAPI → 前端 TypeScript，端到端类型安全
- **📦 开箱即用** - 数据库、认证、日志、错误处理全配置
- **🤖 AI 协作优先** - 完整的 AI 开发规范和项目结构设计
- **🚢 全平台发布** - 支持 Docker 容器化部署和 Windows 原生桌面应用打包
- **⚙️ 灵活配置** - 所有项目信息可通过环境变量定制

---

## 🚀 快速开始

```bash
# 一键初始化
./scripts/init-project.sh

# 启动开发环境
pnpm dev:all

# 访问应用
# 前端: http://localhost:5173
# API文档: http://localhost:9871/docs
# 默认账号: admin / admin
```

详细说明：[快速开始指南](./docs/getting-started.md)

---

## 📚 文档导航

完整文档请访问：**[文档中心](./docs/README.md)**

### 🔥 热门文档

- **[快速开始](./docs/getting-started.md)** - 5 分钟上手
- **[部署指南](./docs/deployment.md)** - Docker / Windows 部署 🆕
- **[开发指南](./docs/development.md)** - 如何开发新功能
- **[命令参考](./docs/commands.md)** - 常用命令速查
- **[AI 协作规范](./.cursor/rules/global.mdc)** - Cursor AI 开发指南

> 更多内容（架构说明、数据库迁移、配置指南等）请查阅 [文档中心](./docs/README.md)。

---

## 🎯 技术栈

**后端**: FastAPI + Pydantic v2 + Tortoise-ORM + Aerich + Loguru + PyInstaller  
**前端**: React 18 + TypeScript 5.6 + Zustand + MUI + React Router v7  
**工具链**: uv (Python) + pnpm (Node.js) + Vite + Docker + GitHub Actions

---

## 📁 项目结构

```
src/
├── features/          # 功能模块（垂直切分）
│   └── user/
│       ├── frontend/  # 前端：页面 + API
│       └── backend/   # 后端：路由 + 模型
├── backend/core/      # 后端核心（安全、日志）
└── frontend/
    ├── core/          # 技术基础设施
    ├── shared/        # 共享业务逻辑
    └── utils/         # 工具函数
```

详细说明：[架构文档](./docs/architecture.md)

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

提交前请确保：

1. 运行 `pnpm type-check` 通过
2. 运行 `pnpm lint:backend` 无错误
3. 遵循开发规范
4. 更新 CHANGELOG.md

---

## 📄 License

MIT License - 自由使用、修改和分发

---

## 🙏 致谢

本模板设计灵感来源于：

- 垂直切分架构（Feature-Sliced Design）
- AI 协作开发最佳实践
- 现代全栈工程化经验

---

**Nekro VStack** - 让 AI 成为你的全栈开发伙伴 🤖✨

**快速开始**: `./scripts/init-project.sh`
