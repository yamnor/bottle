from bottle import Bottle, run

app = Bottle()

@app.get('/')
def index():
  return '<b>Hello world</b>!'

run(app)