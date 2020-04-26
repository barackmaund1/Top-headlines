from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig,)

# app.config.from_pyfile('config.py')
app.config.update(
    DEBUG = True,
    WTF_CSRF_ENABLED = True,
    SECRET_KEY ='0add1611ecf8610320a09ff4b0e34e42'  
)
# Iniializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
from app import error