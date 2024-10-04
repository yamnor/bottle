from bottle import Bottle, template

app = Bottle()

@app.route('/')
def root():
  return template('<b>Hello World</b>!')

@app.route('/hello/<name>')
def root(name):
  return template('<b>Hello {{name}}</b>!', name=name)
