from bottle import Bottle, template

app = Bottle()

@app.route('/')
def index():
  return '<b>Hello world</b>!'

@app.route('/hello/<name>')
def index(name):
  return template('<b>Hello {{name}} world</b>!', name=name)
