from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Top Headlines'
    return render_template('index.html',title=title)
@app.route('/content/<article_id>')
def content():

    '''
    View content page function that returns the news content page and its data
    '''
    return render_template('movie.html')    