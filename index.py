from bottle import route

@route('/')
def index():
  return '<b>Hello world</b>!'
