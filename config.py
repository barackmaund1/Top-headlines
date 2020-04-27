import os

class Config:
    '''
    General configuration parent class
    '''
    TOP_HEADLINES_API_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    EVERYTHING_API_BASE='https://newsapi.org/v2/everything?apiKey={}'
    SECRECT_KEY='0add1611ecf8610320a09ff4b0e34e42'

    SECRECT_KEY=os.environ.get('SECRET_KEY')
    TOP_HEADLINES_API=os.environ.get('TOP_HEADLINES_API')
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}    
