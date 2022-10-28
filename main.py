import os
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
  conn_string = os.environ['CONNECTION_STRING']
  conn = psycopg2.connect(conn_string)
  return conn


@app.route('/')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM movies;')
  movies = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('index.html', movies=movies)

@app.route('/add')
def add():
  return render_template('form.html', action='/create', label='Agregar', post=None)

@app.route('/create', methods=['POST'])
def create():  
  title  = request.form.get('title')
  year = request.form.get('year')
  return f"{title} - {year}"
app.run(host='0.0.0.0', port=8080, debug=True)