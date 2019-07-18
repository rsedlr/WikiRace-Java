import os, json, requests, time
from bottle import route, run, template, static_file, redirect, request, response, put, post, get, error


def findPathTest(data):
  end = data['end'][30:]
  start = data['start'][30:]
  nextItems = [start]
  print('start: %s\nend: %s' %(start, end))
  item = 0
  while end not in nextItems:
    params = {'action':'query', 'format':'json', 'pllimit':'max', 'prop':'links', 'titles':nextItems[item]} 
    first = requests.get(url='https://en.wikipedia.org/w/api.php', params=params).json()  # https://en.wikipedia.org/w/api.php?action=query&titles=England&prop=links&pllimit=max
    a = first['query']['pages']
    b = a[a.keys()[0]]['links']
    for i in range(len(b)):
      nextItems.append(b[i]['title'].replace(' ', '_'))
    print(item)
    item += 1


def findPath(data):
  end = data['end'][30:]
  start = data['start'][30:]
  nextItems = [start]
  print('start: %s\nend: %s' %(start, end))
  params = {'action':'query', 'format':'json', 'pllimit':'max', 'prop':'links', 'titles':nextItems[0]} 
  first = requests.get(url='https://en.wikipedia.org/w/api.php', params=params).json()  # https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&titles=
  a = first['query']['pages']
  b = a[a.keys()[0]]['links']
  for i in range(len(b)):
    nextItems.append(b[i]['title'].replace(' ', '_'))
  print(nextItems)
  print(end in nextItems)


  # s = time.time()
  # e = time.time()
  # print('time taken: %s' %(e-s))

  # firstLinks = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&titles=' + data['start']

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
  findPath(data)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  run(host='127.0.0.1', port=port, debug=True, reloader=True)