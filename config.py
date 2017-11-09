class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

DEBUG = False
SQLALCHEMY_ECHO = False