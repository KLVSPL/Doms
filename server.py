import socket
s = socket.socket()
print('Socket succesfully created')
port = 10242
s.bind(('', port))
print(f'socket binded to port{port}')
s.listen()
print('Socket is listening')
hostname = input("IP:")
port = input("Port:")
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(hostname.encode())
    c.close()
    c, addr = s.accept()
    c.send(port.encode())
    c.close()
