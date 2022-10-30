from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask('__name__')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/users/<string:name>')
def users(name):
  return render_template('users.html', name=name)

bootstrap = Bootstrap(app)