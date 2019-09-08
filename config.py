import os
basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    DEBUG = True
    TESTING = False
    THREADED = True
    SERVER_NAME = '127.0.0.1:5002'
    SQLALCHEMY_DATABASE_URI = os.getenv('sqlalchemy_database_url')

class DevelopmentConfig(DefaultConfig):
    """
    Development configurations
    """
    DEBUG = True
    # SQLALCHEMY_RECORD_QUERIES = False


class ProductionConfig(DefaultConfig):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}