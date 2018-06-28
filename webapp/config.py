class Config(object):
    SECRET_KEY = '5a8e43810ef2d0de40e5f4b86d791f6c'
    RECAPTCHA_PUBLIC_KEY = '6LcyOWAUAAAAANG9YWZB5W5i371ZN1q4yJl59JhB'
    RECAPTCHA_PRIVATE_KEY = '6LcyOWAUAAAAAC8wplV54u6qC60jhW43Qwl85nbs'

class ProConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Zh)D^dlf@39.104.168.95:3306/flask_db'
    SQLALCHEMY_ECHO = True
