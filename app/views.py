from app import app
from database import get_db
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    return render_template('index.html', rows=rows)
