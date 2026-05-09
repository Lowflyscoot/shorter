from sqlalchemy import select, Column, Integer, DateTime, String
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.db.models.links import Link

from app.db.base import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    original_url: Mapped[str] = mapped_column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)