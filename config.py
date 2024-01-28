import os
import pymysql


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'L0wfat'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@127.0.0.1:3306/Activities"
