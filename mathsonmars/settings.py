import tempfile
import os, logging
db_file = tempfile.NamedTemporaryFile()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Config(object):
    # Get the current working directory to place mathsonmars.db during development.
    # In production, use absolute paths or a database management system.
    logger.debug(">>Config()")
    APP_DIR = os.path.abspath(os.curdir)
    SECRET_KEY = os.environ.get('MARS_SECRET_KEY')
    BCRYPT_LOG_ROUNDS = os.environ.get('MARS_BCRYPT_LOG_ROUNDS')
    if BCRYPT_LOG_ROUNDS is None:
        logger.debug("Config error")
    else:
        BCRYPT_LOG_ROUNDS = int(BCRYPT_LOG_ROUNDS)
        logger.debug("Config OK")
    # email server
    MAIL_SERVER = os.environ.get('MARS_MAIL_SERVER')
    MAIL_PORT = os.environ.get('MARS_MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MARS_MAIL_USE_TLS')
    #use SSL throws error when try to send email
    #MAIL_USE_SSL = os.environ.get('MARS_MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MARS_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MARS_MAIL_PASSWORD')
    MAIL_SENDER = os.environ.get('MARS_MAIL_SENDER')
    ADMIN_EMAIL = os.environ.get('MARS_ADMIN_EMAIL')
    LOGGING_FILE = os.environ.get('MARS_LOGGING_FILE')
    EMAIL_TOKEN_SALT = 'confirm_email_token'

    
class ProdConfig(Config):
    logger.debug(">>ProdConfig()")
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('MARS_POSTGRESQL_DATABASE_URI')
    CACHE_TYPE = 'simple'
    WTF_CSRF_ENABLED = True
    
class DevConfig(Config):
    logger.debug(">>DevConfig()")
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('MARS_SQLITE_DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('MARS_POSTGRESQL_DATABASE_URI')
    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = True
    

class TestConfig(Config):
    logger.debug(">>TestConfig()")
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../test_database.db'
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
    

