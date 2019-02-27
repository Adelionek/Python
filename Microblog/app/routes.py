from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
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

    return render_template('index.html', title='Home', posts=posts)
# this makes a callback for {{ user.something}}


@app.route('/login', methods=['GET', 'POST'])
# url_for func takes the below function name
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm() # declaration of login form

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # current user will ne set to that user
        next_page = request.args.get('next')    # collecting the next page sent by client
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html',  title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
