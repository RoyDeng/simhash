import os

from web.app import create_app


env = os.environ.get('APP_ENV')

if not env:
    raise Exception('APP_ENV not found.')

application = create_app(env)
