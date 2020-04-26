class Config:
    '''
    General configuration parent class
    '''
    TOP_HEADLINES_API_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    EVERYTHING_API_BASE='https://newsapi.org/v2/everything?apiKey={}'
    SECRECT_KEY='0add1611ecf8610320a09ff4b0e34e42'

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
