
import socket
import threading


# set up the socket using local address
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket1.bind(('0.0.0.0', 8090))

socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.settimeout(5)
socket2.connect(('192.168.0.142', 5577))

msg = bytearray([0x41])

r = 0
g = 255
b = 0

msg.append(int(r))
msg.append(int(g))
msg.append(int(b))

msg.append(int(0))

write_mask = 0x00

write_mask |= 0xf0
msg.append(write_mask)
msg.append(0x0f)

csum = sum(msg) & 0xFF
msg.append(csum)

while 1:


    data, ip = socket1.recvfrom(1024)

    message = data[0]
    # display


    lock = threading.Lock()


    b = bytearray()
    b.extend(data)
    # b.append(csum)

    print(data)

    with lock:
        socket2.send(msg)


    # echo back
