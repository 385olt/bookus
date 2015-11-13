from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Miguel'} # fake user
	books = [
				{
					'author': {'username': 'Jack'},
					'title': 'Beware, people!',
					'date': '12 November 2015',
					'description': 'It''s a description, read it'
				}
			] * 5
	return render_template('index.html', 
							user=user,
							books=books)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
							form=form)