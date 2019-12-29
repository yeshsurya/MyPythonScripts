# -*- coding: utf-8 -*-
"""
Spyder Editor

@yesh : Site Map

"""

url="https://www.geeksforgeeks.org/"
siteDumpFile="geeksForGeeksFile"

from bs4 import BeautifulSoup
import urllib.request
import re
import signal
import sys

siteMap={}
siteMap[url]=0;
def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        print('Dumping siteMap to file')
        printMapToFile(siteDumpFile,siteMap)
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def printMapToFile(siteDumpFile,siteMap):
    with open(siteDumpFile, 'w') as f:
        for key, value in siteMap.items():
            f.write('%s:%s\n' % (key, value))
    #f.close();
def allVisited(siteMap):
    for site in siteMap:
        if(siteMap[site]==0):
            return False
    return True
def nextUrl(siteMap):
    for site in siteMap:
        if(siteMap[site]==0):
            print("Processing site"+site)
            return site
    return ""
def fillMap(url,siteMap):
    if(url==""):
        return
    if(allVisited(siteMap)):
        return
    else:
        html = urllib.request.urlopen(url)
        siteMap[url]=1
        soup = BeautifulSoup(html)
        for link in soup.find_all('a',attrs={'href': re.compile("^http://")}):
            newLink = link.get('href')
            if newLink not in siteMap:
                siteMap[link.get('href')]=0;
        fillMap(nextUrl(siteMap),siteMap)

if __name__=="__main__":
    fillMap(url,siteMap)
    printMapToFile(siteDumpFile,siteMap)
    f.close();