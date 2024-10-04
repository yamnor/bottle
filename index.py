from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
  return '<b>Hello world</b>!'
