from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Iniializing Flask Extensions
bootstrap = Bootstrap()
def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])

    # app.config.from_pyfile('config.py')
    app.config.update(
        DEBUG = True,
        WTF_CSRF_ENABLED = True,
        SECRET_KEY ='0add1611ecf8610320a09ff4b0e34e42'  
    )


    return app