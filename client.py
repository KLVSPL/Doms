import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "0.tcp.ap.ngrok.io"
server_port = int(input("Enter Server Port:"))

#get ip
s.connect((server_ip, server_port))
hostname = s.recv(1024)
ip = str(hostname.decode())
s.close()
#Get port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))
hostport = s.recv(1024)
port = int(hostport.decode())
s.close()
#Get Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))
proto = s.recv(1024)
protocol = str(proto.decode())
s.close()

print(ip,port,protocol)
