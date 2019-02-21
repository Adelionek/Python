from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John', 'nick': 'Oliwka'},
            'body': 'Beautiful day in Poland!'
        },
        {
            'author': {'username': 'Adam', 'nick': 'Oliwka'},
            'body': 'I bought a cool car!'
        },
        {
            'author': {'username': 'Oliwia', 'nick': 'Oliwka'},
            'body': 'I like dogs :))))'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

