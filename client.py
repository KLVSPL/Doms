import socket
s = socket.socket()
port = 10242
s.connect(('127.0.0.1', port))
ip = s.recv(1024)
s.close()
s = socket.socket()
s.connect(('127.0.0.1', port))
port = s.recv(1024)
s.close()

print(ip.decode(),":",port.decode())