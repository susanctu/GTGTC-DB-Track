import sqlite3
import imdb

def populate_sqlite_db(movieIDFile):
  conn = sqlite3.connect('data/movies.db')
  c = conn.cursor()
  c.execute('DROP TABLE IF EXISTS movies')
  c.execute('CREATE TABLE movies (title text PRIMARY KEY, director text, year integer, rating real)')

  imdbConn = imdb.IMDb()
  with open(movieIDFile, 'r') as idsFile:
    for line in idsFile:
      movie = imdbConn.get_movie(line)
      title = movie['title']
      director = movie['director'][0]['name'] if len(movie['director']) == 1 else (movie['director'][0]['name'] + ' et al.')
      year = movie['year']
      rating = movie['rating']
      c.execute('INSERT INTO movies VALUES (\'%s\', \'%s\', %d, %f)' % (title, director, year, rating))
  conn.commit()
  conn.close()

if __name__ == "__main__":
  populate_sqlite_db('data/mini.txt')
