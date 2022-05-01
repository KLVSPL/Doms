import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "127.0.0.1"
server_port = 10242

#get ip
s.connect((server_ip, server_port))
hostname = s.recv(1024)
print("Host/IP:",str(hostname.decode()))
s.close()
#Get port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))
hostport = s.recv(1024)
print("Port:",int(hostport.decode()))
s.close()
#Get Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))
proto = s.recv(1024)
print("Protocol:",str(proto.decode()))
s.close()

