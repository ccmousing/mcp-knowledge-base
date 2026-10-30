from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


@app.get("/")
def root():
    return {"message": "MCP 知识库问答系统", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
