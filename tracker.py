import socket
import geocoder

hostname =socket.gethostname()
Ip = socket.gethostbyname(hostname)

print("your device name is :" ,hostname)
print("your device ip address is ", Ip)

g=geocoder.ip("me")

print("your latitude and longitude is",g.latlng)