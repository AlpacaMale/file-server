import os


class Config:
    UPLOAD_FOLDER = "uploads"
    SECRET_KEY = "your-secret"
    MAX_STORAGE = 1024 * 1024 * 1024 * 2
    STORAGE_WARNING = int(MAX_STORAGE * 70 / 100)
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
