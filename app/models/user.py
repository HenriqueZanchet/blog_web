from app import db
from datetime import date

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(255), nullable=False)
  sobrenome = db.Column(db.String(255), nullable=False)
  senha = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), unique=True, nullable=False)
  biografia = db.Column(db.Text)
  avatar_url = db.Column(db.String(255))
  data_registro = db.Column(db.Date, default=date.today, nullable=False)
  
  posts = db.relationship('Post', backref='usuario', lazy=True)
  likes = db.relationship('Like', backref='usuario', lazy=True)
  