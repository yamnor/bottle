from bottle import Bottle, template, post

app = Bottle()

@app.post('/hello/<name>')
def index(name):
  return template('<b>Hello {{name}}</b>!', name=name)
