class BaseConfig(object):
    SECRET_KEY = 'make sure to set a very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15
    ADMIN_PER_USER = 9

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/simpledu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
        }
