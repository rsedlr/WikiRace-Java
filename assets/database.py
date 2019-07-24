import os.path, sqlite3

class Database(object):

  def __init__(self, file):
    if not os.path.isfile(file):
      raise IOError('Specified SQLite file "{0}" does not exist.'.format(file))
    else:
      self.conn = sqlite3.connect(file)
      self.cursor = self.conn.cursor()
      self.cursor.arraysize = 1000  # idk


  def getLinksCount(self, linkDirection, pageIDs):
    if linkDirection == 'in':
      sumType = 'incoming_links_count'
    elif linkDirection == 'out':
      sumType = 'outgoing_links_count'
    else:
      raise ValueError('Invalid linkDirection {0} provided, must be \'in\' or \'out\''.format(linkDirection))

    pageIDs = str(tuple(pageIDs)).replace(',)', ')')
    query = 'SELECT SUM({0}) FROM links WHERE id IN {1};'.format(sumType, pageIDs)
    self.cursor.execute(query)

    return self.cursor.fetchone()[0]


  def getLinks(self, linkDirection, pageIDs):
    if linkDirection == 'in':
      sumType = 'incoming_links'
    elif linkDirection == 'out':
      sumType = 'outgoing_links'
    else:
      return None

    pageIDs = str(tuple(pageIDs)).replace(',)', ')')
    query = 'SELECT id, {0} FROM links WHERE id IN {1};'.format(sumType, pageIDs)
    self.cursor.execute(query)

    return self.cursor


  def getPageName(self, pageID):
    query = 'SELECT title FROM pages WHERE id = {0};'.format(pageID)
    self.cursor.execute(query)
    result = self.cursor.fetchall()

    if not result:
      raise ValueError('Invalid page ID {0} provided, page does not exist'.format(pageID))
    
    result = str(result[0])[2:-3]  # trim (' and ,') from result
    return result  # TODO: currently returns sanetized name, revert this to normal