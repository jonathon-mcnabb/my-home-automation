import socket
import threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.settimeout(5)
socket.connect(('192.168.0.142', 5577))

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

lock = threading.Lock()

with lock:
    socket.send(msg)