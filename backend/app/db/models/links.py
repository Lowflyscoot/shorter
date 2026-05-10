from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from .base import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    original_url: Mapped[str] = mapped_column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
