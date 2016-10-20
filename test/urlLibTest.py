#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib2
from libs import funciones
#import urllib2
from bs4 import BeautifulSoup
url = "http://submanga.org/sun-ken-rock"
#f = urllib2.urlopen('http://submanga.org/sun-ken-rock/')
#hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#       'Accept-Encoding': 'none',
#       'Accept-Language': 'en-US,en;q=0.8',
#       'Connection': 'keep-alive'}

#req = urllib2.Request(url, headers=hdr)

#try:
#    page = urllib2.urlopen(req)
#except urllib2.HTTPError, e:
#    print e.fp.read()

http = httplib2.Http()

headers, body = http.request(url)
content = body
#print content
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
#soupTable = soup.find(id="caps-list")
soupTable = soup.find("table", {"id" : "caps-list"})
rows = soupTable.find_all('tr')

for row in rows:
    cells = row.find_all("td")
    txtCont = cells[0].get_text()
    rn = cells[1].a.get("href") 
    dict = {}
    dict["href"] = rn
    dict["txt"] = txtCont
    dict["desc"] =cells[1].get_text().encode('utf-8')
    #cols = row.find_all("td", {"class" : "pad-no hidden-xs"})    
    #cols = [ele.text.strip() for ele in cols]
    #print dict["desc"]
    #print "_________________________"

######## Prueba 2

url = "http://submanga.org/sun-ken-rock/capitulo/6/es"
headers, body = http.request(url)
content = body
#print content
soup = BeautifulSoup(content, 'html.parser')
soupDiv = soup.find("div", {"class" : "pagination-bar"})
totalImgs = soupDiv.get_text().encode('utf-8').replace("/", "")
print totalImgs

