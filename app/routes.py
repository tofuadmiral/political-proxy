from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # here's some fake data to pretend to render our stuff
    user = {'username': 'Fuad'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/get_tweets')
def get_tweets():
    # just pretend to get new tweets
    tweets = ['hello', 'tweet 2', 'tweet3']
    return render_template('get_tweets.html', title='Getting Tweets')
