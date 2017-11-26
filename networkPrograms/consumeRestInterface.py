import  urllib
u = urllib.urlopen('http://localhost:8080/hello?name=Guido')
print(u.read().decode('utf-8'))

u = urllib.urlopen('http://localhost:8080/localtime')
print(u.read().decode('utf-8'))
