import os, json, requests, time
from bottle import route, run, template, static_file, redirect, request, response, put, post, get, error

from search import searchDatabase
from database import Database

dev = False

try:
  database = Database(file='./database/wikiLinks.sqlite')
except:
  dev = True
  print('no database found')


@error(404)
def error404(error):
  return template('error404')

if dev:
  @route('/')
  def rootDir():
    redirect('/wikiRace')

@route('/wikiRace/static/<filepath:path>') 
def server_static(filepath):
  return static_file(filepath, root='./assets')

@route('/wikiRace')
def index():
  return template('race')

@route('/wikiRace/search', method='POST')
def search():
  try:
    data = json.loads(request.body.read().decode("utf-8"))
  except Exception as e:
    print(e)
  routes = []
  end = data['end']
  start = data['start']
  initialTime = time.time()
  # print('\nstart: %s\nend: %s\n' %(start[0], end[0]))
  result = searchDatabase(database, start[1], end[1])

  for route in result:
    temp = []
    for pageID in route:
      temp.append(database.getPageName(pageID)[1:].replace('_', ' '))
    routes.append(temp)
  
  routes.insert(0, time.time() - initialTime)

  return json.dumps(routes)
  


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 3100))
  run(host='127.0.0.1', port=port, debug=True, reloader=True)


'''
TODO
  if imputs are left blank - display appropreate message
  display results with hyperlink
  display results in nicer way
  add buffering animation

'''