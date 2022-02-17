# RPI

import socket

ip_send = "unicorn.cim.mcgill.ca"
#ip_send = "132.206.74.92"
#ip_send = "192.168.43.32"
ip_listen = "0.0.0.0"
receive_port = 14923
send_port = 14923
msg = b"80"

sock_send = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock_receive = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

print(f'Sending {msg} to {ip_send}:{send_port}')
sock_send.sendto(msg, (ip_send, send_port))

sock_receive.bind((ip_listen, receive_port))
print(f'Start listening to {ip_listen}:{receive_port}')

while True:
    data, addr = sock_receive.recvfrom(1024) # buffer
    num = int(data)
    num = num + 1
    print(f"received message: {data}")
    print(f"processed message: {num}")