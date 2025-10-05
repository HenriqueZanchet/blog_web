
from sqlalchemy import String, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from app import db


class User(db.Model):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(30), nullable=False)
    sobrenome: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)
    biografia: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    
    def __repr__(self):
        return f"User(id={self.id} nome={self.nome} email={self.email})"
      
    # Relacionamento com Post --- IGNORE ---
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete-orphan")
    likes: Mapped[list["Like"]] = relationship("Like", back_populates="user", cascade="all, delete-orphan")