import os
from bottle import route, run, template, static_file, redirect, request, response, put, post, get, error


@error(404)
def error404(error):
  return template('error404')

@route('/static/<filepath:path>') 
def server_static(filepath):
  return static_file(filepath, root='./assets')

@route('/')
def index():
  return template('race')

@route('/search', method='POST')
def search():
  data = (request.body.read().decode("utf-8"))
  print(data)
  # print(data[2])
  # start, end = data[0], data[1]
  # start, end = request.body.readlines()
  # print('start: ' + start + '\nend: ' + end)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  run(host='127.0.0.1', port=port, debug=True, reloader=True)