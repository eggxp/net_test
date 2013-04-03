#!/usr/bin/python
import socket
import threading

a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a.bind(("0.0.0.0",8888))
send_msg = '0123456789' * 50;
while True:
    msg, addr = a.recvfrom(1024)
    if msg.endswith('#'):
      msg = msg[:len(msg)-1]
      if len(msg) > 0:
        a.sendto(msg, 0, addr)
      for _ in range(8):
        a.sendto(send_msg, 0, addr)
      a.sendto(send_msg+'#', 0, addr)
    else:
      a.sendto(msg, 0, addr)
    print addr


