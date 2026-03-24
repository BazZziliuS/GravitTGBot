from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Integer, Text, Index, func
from sqlalchemy.orm import Mapped, mapped_column

from tgbot.database.models.base import Base


class Task(Base):
    __tablename__ = "storage_tasks"
    __table_args__ = (
        Index("ix_tasks_user_active", "user_id", "done"),  #ty gravit
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    text: Mapped[str] = mapped_column(Text)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
