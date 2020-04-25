from flask import render_template
from app import app
from .request import get_sources,get_headlines

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting the general sources
    general_source=get_sources('general')
    business=get_sources('business')
    entertainment=get_sources('entertainment')
    sport=get_sources('sports')
    technology=get_sources('technology')
    title='Top Headlines'
    return render_template('index.html',title=title,general=general_source,business=business,entertainment=entertainment,sport=sport,technology=technology)
@app.route('/articles/<id>')
def Headlines(id):

    '''
    View content page function that returns the news content page and its data
    '''
    headlines_articles=get_headlines(id)
    source=id
    
    return render_template('headlines.html',articles=headlines_articles,source=source)    