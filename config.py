import os
import pymysql


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL' or
                                             "test")
