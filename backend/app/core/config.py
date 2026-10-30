from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    # 项目
    PROJECT_NAME: str = "MCP 知识库问答系统"
    API_V1_STR: str = "/api/v1"

    # 安全
    SECRET_KEY: str = "changethis-please-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 数据库
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/knowledge_base"

    # 前端
    FRONTEND_HOST: str = "http://localhost:5173"

    # 初始管理员
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "changethis"

    # LLM 配置
    LLM_API_KEY: str = ""
    LLM_BASE_URL: str = "https://api.deepseek.com"
    LLM_MODEL: str = "deepseek-chat"

    # Embedding
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    HF_ENDPOINT: str = "https://hf-mirror.com"

    # 向量库
    VECTOR_DB_PATH: str = "./chroma_data"


settings = Settings()
