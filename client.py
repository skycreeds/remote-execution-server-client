#@skycreeds
import socket
import sys
buffer_size=1024*128

#1
target_host = '192.168.80.1'
target_port = 99
#2
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
#3
while True:
    data=client.recv(buffer_size).decode()
    print(data)
    data=input(">>>")
    client.sendall(data.encode())

