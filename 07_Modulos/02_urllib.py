
"""
import urllib
url = 'http://diveintomark.org/projects/feed_parser/feedparser.py'
arq = urllib.urlopen(url)
open('feedparser.py', 'w').write(arq.read())

with urllib.request.urlopen(b"http://www.python.org".decode('utf-8')) as url:

"""


import urllib.request
import feedparser

with urllib.request.urlopen("http://diveintomark.org/projects/feed_parser/feedparser.py") as url:
    arq = url.read()

    # AttributeError: 'bytes' object has no attribute 'read'
    # open('feedparser.py', 'w').write(arq.read())
    print(arq)

terra = feedparser.parse('http://rss.terra.com.br/0,,EI1,00.xml')
print(terra.values())

