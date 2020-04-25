from app import app

import urllib.request,json
from .models import article,source,top_headlines

Article=article.Article
Source=source.Source
Top_headlines=top_headlines.Top_headlines
#Getting the api key
api_key='e5847b6ab9a643469ea467c6e7965d8c'

#Getting the Article base url
article_url=app.config['EVERYTHING_API_BASE']
source_url=app.config['SOURCE_API_BASE_URL']
top_headlines_url=app.config['TOP_HEADLINES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url=source_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data) 

        source_results=None

        if get_sources_response['sources']:
            source_results_list=get_sources_response['sources']
            source_results=process_results(source_results_list)


    return source_results 

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results=[]
    for source_item in source_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category=source_item.get('category')
        language=source_item.get('language')
        country=source_item.get('country')

        
        source_object=Source(id,name,description,url,category,language,country)
        source_results.append(source_object)


    return source_results

def get_headlines(source):
    
    get_article_url=top_headlines_url.format(article,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        article_data=url.read()
        article_response=json.loads(article_data)

        article_results=None

        if article_response["articles"]:
            article_results_list=article_response['articles']
            article_results=process_new_articles(article_results_list)
    return article_results  

def process_new_articles(article_list):

    article_results=[]

    for item_article in article_list:
        source=item_article.get('source')
        author=item_article.get('author')
        description=item_article.get('description')
        title=item_article.get('title')
        url=item_article.get('url')
        urlToImage=item_article.get('urlToImage')
        publishedAt=item_article.get('publishedAt')
        content=item_article.get('content')

        new_article=Article(source,author,description,title,url,urlToImage,publishedAt,content)
        article_results.append(new_article)

    return article_results    





