import socket
import sys

# Creem un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Definim la adreça ip i el port de la conexio
server_address = ('localhost', 10000)
#FALTA INTRODUIR AQUEST PARAMETRE VIA TERMINAL AMB EL SYS.ARGV QUE NOSE COM VA
message = 'estat'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
