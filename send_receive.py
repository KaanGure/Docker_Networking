# SERVER

import socket

#ip_send = "10.126.138.225"
ip_send = "192.168.43.32"
ip_receive = "0.0.0.0"
receive_port = 14923
send_port = 14923


sock_send = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock_receive = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock_receive.bind((ip_receive, receive_port))

while True:
    print('Start listening to ' + str(ip_receive) + ':' + str(receive_port))
    data, addr = sock_receive.recvfrom(1024) # buffer
    print('recv_addr = ' + str(addr))
    #process
    num = int(data)
    num = num + 1
    msg = (bytes(str(num), 'utf8'))
    print('received message: ' + str(data))
    print('processed message: ' + str(num))
    #send back
    print('Sending ' + str(msg) + ' to ' + str(ip_send) + ':' + str(send_port))
    sock_send.sendto(msg, (ip_send, send_port))