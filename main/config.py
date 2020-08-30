import os

class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class ProductionConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('postgres://xrknyfisbwkkke:6f48bc1dcc9888a28f590ec769c76ebaf24c90dc9ad285993e9351fe3ca6e555@ec2-107-20-15-85.compute-1.amazonaws.com:5432/dd759lo3k7m13o')

config = {
    "default": "main.config.BaseConfig",
    "development": "main.config.DevelopmentConfig",
    "production": "main.config.ProductionConfig",
}

def configure_app(app):
    config_name= os.getenv('FLASK_ENV')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('application.cfg', silent=True)