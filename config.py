import os
import dotenv


base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(base_dir, '.env'))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = 'Web notification App'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Set a secret key, this is important!')
    TOKEN = os.environ.get('TOKEN', 'Specify telegram bot token!')
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
    MONGO_NAME = os.environ.get('MONGO_NAME', 'telegram_db')

    @staticmethod
    def configure(app):
        with app.app_context():
            host = app.config.get('MONGO_HOST', 'localhost')
            port = app.config.get('MONGO_PORT')
            name = app.config.get('MONGO_NAME')
            token = app.config.get('TOKEN')

            mongo_uri = 'mongodb://%s:%s/%s' % (host, port, name)

            app.config['WEBHOOK_URL'] = '/%s/' % token
            app.config['MONGO_URI'] = mongo_uri


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""


config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig)
