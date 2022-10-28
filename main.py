import os
from flask import Flask, render_template, request, redirect, abort
import psycopg2

app = Flask(__name__)

def get_db_connection():
  conn_string = os.environ['CONNECTION_STRING']
  conn = psycopg2.connect(conn_string)
  return conn

def get_movie(movie_id):
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute(f"SELECT * FROM movies WHERE id = {movie_id}")
  movie = cur.fetchone()
  conn.close()
  if movie is None:
     abort(404)
    
  return {'id': movie[0], 'title': movie[1], 'year': movie[2], 'director': movie[3], 'rating': movie[4], 'review': movie[5]}

@app.route('/')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM movies ORDER by id;')
  movies = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('index.html', movies=movies)

@app.route('/add')
def add():
  return render_template('form.html', action='/create', label='Agregar', movie=None)

@app.route('/create', methods=['POST'])
def create():  
  title  = request.form['title']
  year = tryint(request.form['year'])
  director = request.form['director']
  rating = tryint(request.form['rating'])
  review = request.form['review']
  if title > '' and year > 0 and director > '':
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO movies (title, year, director, rating, review)'
            'VALUES (%s, %s, %s, %s, %s)',
            (title, year, director, rating, review))
    conn.commit()
    conn.close()
  return redirect('/')
  
@app.route('/edit/<int:id>')
def edit(id):
  movie = get_movie(id)
  return render_template('form.html', action='/save', movie=movie, label='Modificar')

 
@app.route('/save', methods=['POST'])
def save():
  id = request.form['id']
  title  = request.form['title']
  year = tryint(request.form['year'])
  director = request.form['director']
  rating = tryint(request.form['rating'])
  review = request.form['review']
  if title > '' and year > 0 and director > '':
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE movies SET title=%s, year=%s, director=%s, rating=%s, review=%s WHERE id = %s',
            (title, year, director, rating, review, id))
    conn.commit()
    conn.close()
  return redirect('/')
  

def tryint(s):
  try:
    return int(s)
  except:
    return 0


app.run(host='0.0.0.0', port=8080)