import os, json, requests, time
from bottle import route, run, template, static_file, redirect, request, response, put, post, get, error

# from assets.database import Database

''' useless '''
def findPath(data):  # not worth trying
  end = data['end'][30:]
  start = data['start'][30:]
  nextItems = [start]
  print('start: %s\nend: %s' %(start, end))
  params = {'action':'query', 'format':'json', 'pllimit':'max', 'prop':'links', 'titles':nextItems[0]} 
  first = requests.get(url='https://en.wikipedia.org/w/api.php', params=params).json()  
  a = first['query']['pages']
  b = a[a.keys()[0]]['links']
  for i in range(len(b)):
    nextItems.append(b[i]['title'].replace(' ', '_'))
  print(nextItems)
  print(end in nextItems)

  # s = time.time()
  # e = time.time()
  # print('time taken: %s' %(e-s))


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
  try:
    data = json.loads(request.body.read().decode("utf-8"))
  except Exception as e:
    print(e)
  end = data['end']
  start = data['start']
  print('start: %s\nend: %s' %(start[0], end[0]))

  # findPath(data)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  run(host='127.0.0.1', port=port, debug=True, reloader=True)



  '''
  main link: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&titles=

  
  '''