class Config(object):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    PORT = 8080
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

