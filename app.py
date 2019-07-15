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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='127.0.0.1', port=port, debug=True, reloader=True)