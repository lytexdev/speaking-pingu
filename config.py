import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "!@?Sup€rS€cretK€y?@!")
    PORT = int(os.getenv("PORT", 5000))
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5000").split(",")

    DEEPSEEK_URL = os.getenv("DEEPSEEK_URL", "http://localhost:11434/api/generate")
    DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-r1:7b")

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False").lower() == "true"

    MAX_LOGIN_ATTEMPTS = int(os.getenv("MAX_LOGIN_ATTEMPTS", 5))
    LOCKOUT_DURATION_MINUTES = int(os.getenv("LOCKOUT_DURATION_MINUTES", 20))
