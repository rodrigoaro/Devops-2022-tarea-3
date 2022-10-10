from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<p>Hola, Mundo!</p>"
  
app.run(host='0.0.0.0', port=8080)