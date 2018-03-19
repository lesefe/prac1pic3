#importem la llibreria per crear els sockets
import socket
import sys

#contador utilitzat despres PER SABER SI EM EXECUTAT EL CODI ABANS
pene = 0

#Creem un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Li donem al socket la informacio del servidor(adress_ip, port)
server_address = ('localhost', 10000)

#Mostrem la ip i el port del servidor
print >> sys.stderr, 'starting up on %s port %s' % server_address
#Nose que fa pero sense aico no tira
sock.bind(server_address)

#Bucle del programa que espera un missatge i si rep algun dato li respon
while True:
    print >> sys.stderr, '\nwaiting to receive message'
    #Guardem el dato rebut i la ip que ens l'envia
    data, address = sock.recvfrom(4096)


    if data:
        #Mostrem el dato enviat
        print >> sys.stderr, data

            #Si hem rebut dato i es on
        if data == 'on' or data == 'ON' or data == 'On':
            estatLed = "on"
            print >> sys.stderr, 'Has engegat el LED'
            pene = 1
            #QUI CANVII NOM DE LA VARIABLE EL REBENTO
            #AQUI FALTA CRIDAR LA FUNCIO QUE FA ENGEGAR EL LED

        #Si hem rebut dato i es off
        elif data == 'off' or data == 'OFF' or data == 'Off' :
            estatLed = "off"
            print >> sys.stderr, 'Has apagat el LED'
            pene = 1
            #QUI CANVII NOM DE LA VARIABLE EL REBENTO
            #AQUI FALTA CRIDAR LA FUNCIO QUE FA APGAR EL LED

        #Si pregunten com esta el led
        elif data == 'status' or data == 'Status' or data == 'Estat' or data == 'estat' :
            if pene == 0:
                estatLed = 'MAI HAS ENGEGEGAT EL LED EN AMB AQUEST CODI O SIGUI QUE HAURIA DE ESTAR APAGAT'
                sent = sock.sendto(estatLed, address)
                print >> sys.stderr, 'El led esta %s ' % (estatLed)

            else :
                sent = sock.sendto(estatLed, address)
                print >> sys.stderr, 'El led esta %s ' % (estatLed)
