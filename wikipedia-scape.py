from bs4 import BeautifulSoup
import urllib2
import re

wiki = "http://en.wikipedia.org/wiki/Mad_Max:_Fury_Road"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)

rnd = ""
pick = ""
NFL = ""
player = ""
pos = ""
college = ""
conf = ""
notes = ""

table = soup.find("table", { "class" : "wikitable sortable" })

print table

#output = open('output.csv','w')

for row in table.findAll("tr"):
    cells = row.findAll("href")
    for cell in cells:
    #   search-term = re.search(r'director',cell)
    #   if search-term:
    #      print search-term
    #print "---"
       print cell.text
    print cells.text
    #print "---"
