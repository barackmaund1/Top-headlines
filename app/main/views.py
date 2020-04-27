from flask import render_template,request,redirect,url_for,flash
from . import main
from ..request import get_sources,get_headlines,search_source
from .form import RegistrationForm,LoginForm
from ..models import Source,Top_headlines,Article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting the general sources
    general_source=get_sources('general')
    health=get_sources('health')
    entertainment=get_sources('entertainment')
    sport=get_sources('sports')
    technology=get_sources('technology')
    title='Top Headlines'
    search_source=request.args.get('source_query')

    if search_source:
        return redirect(url_for('search',source_name=search_source))

    else:
        return render_template('index.html',title=title,general=general_source,health=health,entertainment=entertainment,sport=sport,technology=technology)
@main.route('/articles/<id>')
def Headlines(id):

    '''
    View content page function that returns the news content page and its data
    '''
    headlines_articles=get_headlines(id)
    source=id
    
    return render_template('headlines.html',articles=headlines_articles,source=source)    


@main.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list=source_name.split(' ')
    source_name_format='-'.join(source_name_list)
    searched_sources=search_source(source_name_format)
    title=f'search results for {source_name}'
    return render_template('search.html',sources=searched_sources ,title=title)

@main.route('/register',methods=['GET','POST']) 
def register() :
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!'),'success'
        return redirect(url_for('index'))
    return render_template('register.html',title='Register',form=form)

@main.route('/login') 
def login() :
    form=LoginForm()
    return render_template('login.html',title='login',form=form)
