#! ../env/bin/python

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader
from flask_wtf.csrf import CsrfProtect


from mathsonmars import assets
from mathsonmars.main import main_view
from mathsonmars.application import appl_view
from mathsonmars.report import report_view
from mathsonmars.auth import auth_view
from mathsonmars.models import Base, db
from mathsonmars.email import mail
from mathsonmars.marslogger import setup_logging

from mathsonmars.extensions import (
    cache,
    assets_env,
    #debug_toolbar,
    bcrypt
)
from mathsonmars.auth.authview import login_manager


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. mathsonmars.settings.ProdConfig
    """
    print(">>create_app object_name:{0}, __name__:{1}".format(object_name, __name__))
    app = Flask(__name__)
    app.config.from_object(object_name)
    #enable CSRF protection for all view handlers
    csrf = CsrfProtect(app)

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    #debug_toolbar.init_app(app)
    
    bcrypt.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)
    
    login_manager.init_app(app)
    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)
        
    # register our blueprints
    app.register_blueprint(main_view)
    app.register_blueprint(auth_view)
    app.register_blueprint(appl_view)
    app.register_blueprint(report_view)

    mail.init_app(app)
    setup_logging(app)
    print("<<create_app")
    return app
