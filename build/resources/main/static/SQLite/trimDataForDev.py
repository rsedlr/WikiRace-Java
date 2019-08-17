import sqlite3, os.path

file = './wikiLinks.sqlite'

if not os.path.isfile(file):
  raise IOError('Specified SQLite file "{0}" does not exist.'.format(file))


conn = sqlite3.connect(file)

c = conn.cursor()
c.arraysize = 1000 

print('deleting * from pages where id > 3000')
conn.execute('DELETE FROM pages WHERE id > 3000;')
print('delete successful')

print('\ndeleting * from redirects where source_id > 3000')
conn.execute('DELETE FROM redirects WHERE source_id > 3000;')
print('delete successful')

print('\ndeleting * from links where id > 3000')
conn.execute('DELETE FROM links WHERE id > 3000;')
print('delete successful')

print('\removing empty space')
conn.isolation_level = None
conn.execute('VACUUM')
conn.isolation_level = '' 
print('removal successful')

conn.commit()
conn.close()

print('\nRenaming to \'wikiLinksDev.sqlite\'')
os.rename('wikiLinks.sqlite', 'wikiLinksDev.sqlite')

print('\nAll done!')



