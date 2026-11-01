import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'postgres')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'postgres')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')
    DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')