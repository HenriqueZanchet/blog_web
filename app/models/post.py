from sqlalchemy import String, Text, Date, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from .. import db

class Post(db.Model):
    __tablename__ = "post"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(255), nullable=False)
    corpo: Mapped[str] = mapped_column(Text, nullable=False)
    data_criacao: Mapped[date] = mapped_column(Date, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    
    def __repr__(self):
        return f"Post(id={self.id} titulo={self.titulo} data_criacao={self.data_criacao})"