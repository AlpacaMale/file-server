class Config:
    UPLOAD_FOLDER = "uploads"
    SECRET_KEY = "your-secret"
    MAX_STORAGE = 1024 * 1024 * 1024 * 2
    STORAGE_WARNING = int(MAX_STORAGE * 70 / 100)
