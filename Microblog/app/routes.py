from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
