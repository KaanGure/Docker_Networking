# SERVER

import socket

ip = "127.0.0.1"
receive_port = 5000
send_port = 5001


sock_send = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock_receive = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock_receive.bind((ip, receive_port))

while True:
    print('Start listening to ' + str(ip) + ':' + str(receive_port))
    data, addr = sock_receive.recvfrom(1024) # buffer
    #process
    num = int(data)
    num = num + 1
    msg = (bytes(str(num), 'utf8'))
    print('received message: ' + str(data))
    print('processed message: ' + str(num))
    #send back
    print('Sending ' + str(msg) + ' to ' + str(ip) + ':' + str(send_port))
    sock_send.sendto(msg, (ip, send_port))