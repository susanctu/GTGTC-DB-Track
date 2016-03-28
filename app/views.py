from app import app
from database import get_db

@app.route('/')
@app.route('/index')
def index():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM movies LIMIT 1")
    result = "%s, directed by %s (%d). %s. Score: %f"  % cursor.fetchone()
    print(result)
    return result
