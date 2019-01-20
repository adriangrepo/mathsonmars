import os
from mathsonmars import create_app


env = os.environ.get('MARS_ENV', 'prod')
app_name = 'mathsonmars.settings.%sConfig' % env.capitalize()
app = create_app(app_name)
