from app import app
from database import get_db
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    cursor = get_db().cursor()
    cursor.execute("[QUERY HERE]")
    rows = cursor.fetchall()
    return render_template(
      'index.html', 
      colnames=('Movie', 'Director', 'Year', 'Rating'), 
      rows=rows)

@app.route('/join')
def join():
    cursor = get_db().cursor()
    cursor.execute("SELECT name,movies.title,rating FROM movies INNER JOIN actors ON movies.title=actors.title")
    rows = cursor.fetchall()
    return render_template(
      'index.html', 
      colnames=('Name', 'Movie', 'Rating'), 
      rows=rows)
