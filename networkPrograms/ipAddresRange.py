import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
#ipaddress.IPv4Address('123.45.67.64/27')
print("All ip addresses in this subnet are : ")
for a in net:
 print(a)