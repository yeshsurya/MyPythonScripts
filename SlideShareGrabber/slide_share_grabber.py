import urllib2
import re
import os

from os.path import basename

from urlparse import urlsplit

from urlparse import urlparse

from posixpath import basename,dirname

## function that processes url, if there are any spaces it replaces with '%20' ##


def process_url():

    if not os.path.exists('images'):
        os.mkdir("images")
        os.mkdir("images/"+dirname)
        os.chdir("images/"+dirname)
    for cnt in range(1,57,1):
        url='https://image.slidesharecdn.com/executive-l-1233675569588726-2/95/executives-'
        url+=str(cnt)
        url+='-728.jpg?cb=1233654034'
        filename="image-"
        filename+=str(cnt)
        filename+=".jpg"
        parse_object=urlparse(url)

        urlcontent=urllib2.urlopen(url).read()

        try:
            output=open(filename,'wb')
            output.write(urlcontent)
            output.close()
        except:
            pass

process_url()