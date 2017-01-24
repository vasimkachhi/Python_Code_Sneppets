"""
    This code crawls two sites and extracts tables and its content using beautiful soup and urllib2
    Crawling or web scrapping example
    1) http://zevross.com/blog/2014/05/16/using-the-python-library-beautifulsoup-to-extract-data-from-a-webpage-applied-to-world-cup-rankings/
    2) https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India
"""



import urllib2
from bs4 import BeautifulSoup
url = "http://zevross.com/blog/2014/05/16/using-the-python-library-" \
      "beautifulsoup-to-extract-data-from-a-webpage-applied-to-world-cup-rankings/"
r = urllib2.urlopen(url)
soup = BeautifulSoup(r, "html.parser")
nested_html = soup.prettify()
data = soup.find("table", {"class": 'sortable'})
datakeylist = []
datadict = []
for row in data.findAll("tr"):
    thh = row.findAll('th')
    tdd = row.findAll('td')
    if thh:
        for t in thh:
            print t.text
            datakeylist.append(t.text)
    if tdd:
        row = {}
        for index, t in enumerate(tdd):
            print t.text
            row.update({datakeylist[index]: t.text})
        datadict.append(row)
print datadict


import urllib2
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
r = urllib2.urlopen(url)
soup = BeautifulSoup(r, "html.parser")
nested_html = soup.prettify()
data = soup.find("table", {"class": 'wikitable sortable plainrowheaders'})
datakeylist = []
datadict = []
for index, row in enumerate(data.findAll("tr")):
    thh = row.findAll("th")
    tdd = row.findAll('td')
    if index < 1:
        for t in thh:
            datakeylist.append(str(t.text).replace('\n', ' '))
        datakeys = datakeylist[:]
        datakeylist.pop(1)
    else:
        roww = {}
        missing = row.findNext('a').text
        for index1, t in enumerate(tdd):
            roww.update({datakeylist[index1]: t.text})
        roww.update({datakeys[1]: missing})
        datadict.append(roww)
print datadict

