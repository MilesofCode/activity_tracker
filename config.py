import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'L0wfat'
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               "mysql+mysqldb://root:admin@127.0.0.1:3306/Activities")
