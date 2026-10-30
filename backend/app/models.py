import uuid
from datetime import datetime, UTC

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    "Field(...):告诉 SQLModel 这是数据库字段，加配置 default_factory=uuid.uuid4:新建记录时，自动调用 `uuid4()` 生成随机 ID"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str
    hashed_password: str
    full_name: str | None = None
    is_active: bool = True
    is_superuser: bool = False
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
