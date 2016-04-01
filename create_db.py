import sqlite3
import imdb

def populate_sqlite_db(movieIDFile):
  conn = sqlite3.connect('data/movies.db')
  c = conn.cursor()
  c.execute('DROP TABLE IF EXISTS actors')
  c.execute('DROP TABLE IF EXISTS movies')
  c.execute('CREATE TABLE movies (title text PRIMARY KEY, director text, year integer, rating real)')
  c.execute('CREATE TABLE actors (name text, title text, id text, FOREIGN KEY(title) REFERENCES movies(title))')

  imdbConn = imdb.IMDb()
  with open(movieIDFile, 'r') as idsFile:
    for line in idsFile:
      movie = imdbConn.get_movie(line)
      title = movie['title']
      director = movie['director'][0]['name'] if len(movie['director']) == 1 else (movie['director'][0]['name'] + ' et al.')
      year = movie['year']
      rating = movie['rating']
      c.execute('INSERT INTO movies VALUES (?, ?, ?, ?)', (title, director, year, rating))
      for castmember in movie['cast']:
        personID = castmember.personID
        name = castmember.data['name']
        c.execute('INSERT INTO actors VALUES (?, ?, ?)', (name, title, personID))
  conn.commit()
  conn.close()

if __name__ == "__main__":
  populate_sqlite_db('data/great_recent_movies.txt')
