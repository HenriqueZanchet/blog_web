from sqlalchemy import String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app import db

class Post(db.Model):
    __tablename__ = "post"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(255), nullable=False)
    corpo: Mapped[str] = mapped_column(Text, nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    
    autor: Mapped["User"] = relationship("User", back_populates="posts")
    likes: Mapped[list["Like"]] = relationship("Like", back_populates="post", cascade="all, delete-orphan")
    