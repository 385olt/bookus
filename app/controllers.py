from flask import render_template, flash, redirect, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm
from .models import User

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/')
@app.route('/index')
def index():
	user = g.user
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
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return redirect(url_for('index'))
	return render_template('login.html',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
