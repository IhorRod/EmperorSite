from app import app
from flask import render_template, flash, redirect


@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    menu = {
        'Головна сторінка': '/',
        'Лібраріум': '#',
        'Імперський вісник': '#',
        'Контакти': '#',
        'Допомога проекту': '#'
    }
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts,
                           menu=menu)

