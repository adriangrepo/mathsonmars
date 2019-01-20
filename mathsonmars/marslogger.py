#to get logger
from werkzeug.local import LocalProxy
from flask import current_app
#from logging import getLogger, Formatter
import logging
from logging.handlers import RotatingFileHandler 
from mathsonmars.settings import Config

def setup_logging(app):
    #TODO fix this hack
    if Config.LOGGING_FILE is None:
        print("Error Config.LOGGING_FILE not set")
    else:
        file_handler = RotatingFileHandler(Config.LOGGING_FILE)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.DEBUG)

        loggers = [app.logger]
        for logger in loggers:
            logger.addHandler(file_handler)

logger = LocalProxy(lambda: current_app.logger)
