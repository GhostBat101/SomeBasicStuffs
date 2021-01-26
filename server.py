import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))
s.listen(3)
print('Waiting for Connection from the client')


while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected with The address: ', addr,' And Name: ', name)
    c.send(bytes('Welcome to the server', 'utf-8'))

    c.close()