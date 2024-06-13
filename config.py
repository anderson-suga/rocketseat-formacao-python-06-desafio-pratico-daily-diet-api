import os


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin123@localhost:3362/daily-diet"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
