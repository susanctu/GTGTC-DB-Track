from app import app
from database import get_db
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    cursor = get_db().cursor()
    cursor.execute("[QUERY 1]")
    rows = cursor.fetchall()
    return render_template(
      'index.html', 
      colnames=('Movie', 'Director', 'Year', 'Rating'), 
      rows=rows)

@app.route('/join')
def join():
    cursor = get_db().cursor()
    cursor.execute("[QUERY 3]")
    rows = cursor.fetchall()
    return render_template(
      'index.html', 
      colnames=('Name', 'Movie', 'Rating'), 
      rows=rows)
