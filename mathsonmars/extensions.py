from flask.ext.cache import Cache
#from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask_assets import Environment
from flask.ext.bcrypt import Bcrypt
#from flask_socketio import SocketIO


# Setup flask cache
cache = Cache()

# init flask assets
assets_env = Environment()
#debug_toolbar = DebugToolbarExtension()
bcrypt = Bcrypt()
#socketio = SocketIO()


