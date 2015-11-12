from flask import render_template
from app import app

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