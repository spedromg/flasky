from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World,  Flask Python! <a href="http://127.0.0.1:5000/user">usuário</a></h1>'

def user():
  return '<h1>Eu sou o usuário Simão Pedro.</h1>'

def user_id(name):
  return f'<h1>Eu sou o usuário {name}.</h1>'

def browsers():
  user_agent =  request.headers.get('User-Agent')
  return f'<h3>Seu browser é {user_agent}</h3>'

app.add_url_rule('/user', 'user', user)
app.add_url_rule('/user_id/<name>', 'user_id', user_id)
app.add_url_rule('/browsers', 'browsers', browsers)

if __name__ == "__main__":
  app.run(debug=True)
