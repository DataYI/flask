class Config(object):
    SECRET_KEY = '5a8e43810ef2d0de40e5f4b86d791f6c'

class ProConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Zh)D^dlf@39.104.168.95:3306/flask_db'
    SQLALCHEMY_ECHO = True
