import socket
s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))
s.listen(3)
print('waiting for connections')

while True:
    c, address = s.accept()
    print("Connected to GTPL.")
    c.send('welcome to GTPL')
    