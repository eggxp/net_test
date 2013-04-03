#!/usr/bin/python

#500kb/s

import socket
import threading
import time


send_msg = '0123456789' * 50 + '#'
recv_msg = '0123456789' * 50 * 10 + '#'

class ThreadClass(threading.Thread):
    def __init__(self, sock):
        self.sock = sock
        threading.Thread.__init__(self)
    def run(self):
      while True:
        try:
          tmp, addr = sock.recvfrom(1024)
          if not tmp:
            continue
        except Exception:
          continue


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a = ThreadClass(sock)
a.start()
cnt = 0
while True:
  sendmsg = '%s:%s:%s' % (cnt, time.clock(), send_msg)
  sock.sendto(sendmsg, ('123.58.171.152', 8889))
  #sock.sendto(sendmsg, ('123.58.171.152', 8889))
  cnt += 1
  time.sleep(0.01)

