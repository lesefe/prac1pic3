import socket
UDP_IP = "172.16.0.136"
UDP_PORT = 10000
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP# Internet
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
