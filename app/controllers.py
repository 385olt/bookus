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
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remeber_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])
