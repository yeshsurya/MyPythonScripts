from urllib import request, parse
# Base URL being accessed
url = 'http://www.google.com'
# Dictionary of query parameters (if any)
parms = {
 'name1' : 'value1',
 'name2' : 'value2'
}
# Encode the query string
querystring = parse.urlencode(parms)
# Make a GET request and read the response
#u = request.urlopen(url+'?' + querystring)
u = request.urlopen(url)
resp = u.read()
print(resp)
