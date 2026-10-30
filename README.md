# MCP 知识库问答系统

基于 MCP（Model Context Protocol）协议的企业级知识库问答系统。

## 功能规划

- [ ] 文档上传（PDF / Word / Markdown）
- [ ] 文档自动切块与向量化
- [ ] RAG 知识库问答
- [ ] MCP 工具封装（搜索、读取文档、历史记录）
- [ ] 用户认证与权限管理
- [ ] 问答历史记录
- [ ] Docker 部署

## 技术栈

- 后端：FastAPI + FastMCP
- 数据库：PostgreSQL + SQLModel
- 向量库：Chroma
- 认证：JWT
- 部署：Docker Compose

## 快速开始

### 后端开发

```bash
cd backend
uv sync
uv run fastapi dev app/main.py --reload
```

访问：
- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/health

## 项目结构

```
mcp-knowledge-base/
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI 入口
│   │   ├── api/routes/       # REST 路由
│   │   ├── core/             # 配置、数据库、安全
│   │   ├── alembic/          # 数据库迁移
│   │   └── mcp_server.py     # MCP 服务器（待开发）
│   └── pyproject.toml
├── frontend/
├── docs/
└── README.md
```
