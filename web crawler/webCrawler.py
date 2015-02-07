from bs4 import *
import urlparse
import urllib2
import os.path
import time


url = "http://www.ccs.neu.edu/"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Connection': 'keep-alive'}
urls = [url]
visited = [url]
extlist = ['.html','.pdf','.xhtml','htm']
domainlist = ['myneu.neu.edu','prod-web.neu.edu','www.northeastern.edu','www.ccs.neu.edu','howto.ccs.neu.edu']
i = 0
proxies = {'http': 'http://proxy.example.com:8080/'}
while len(visited) <= 100:
    time.sleep(5)
    htmltext = ""
    try:
        req = urllib2.Request(urls[0],headers = {'User-Agent': 'Mozilla/5.0'})
        htmltext = urllib2.urlopen(req).read()
    except:
        print "Exception"
        
    soupObj = BeautifulSoup(htmltext)
    for tag in soupObj.findAll("a",href=True):      
        o = urlparse.urlsplit(tag['href'])
        fileNameAndExt = os.path.splitext(os.path.basename(urlparse.urlsplit(tag['href']).path))
        if tag['href'] != '#':
            req = urllib2.Request(tag['href'],headers = {'User-Agent': 'Mozilla/5.0'})
            htmltext = urllib2.urlopen(req).read()
            soupObjTwo = BeautifulSoup(htmltext)
            if soupObjTwo.find("html") is not None:
                visited.append(tag['href'])
            elif fileNameAndExt[1] in extlist and tag['href'] not in visited:
                visited.append(tag['href'])
            urls.append(tag['href'])

        else:
            continue
            
            
print visited
  

        
        
        