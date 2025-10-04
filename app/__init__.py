from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from app import models

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  
  # Inicializar extensões
  db.init_app(app)
  migrate.init_app(app, db)
  
  # Registrar blueprints (views) aqui depois
  
  return app