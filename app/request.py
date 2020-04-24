from app import app

#Getting the api key
api_key=app.config["TOP_HEADLINES_API_KEY"]

#Getting the Article base url
article_url=app.config['EVERYTHING_API_BASE']
source_url=app.config['SOURCE_API_BASE_URL']
top_headlines_url=app.config['TOP_HEADLINES_API_BASE_URL']