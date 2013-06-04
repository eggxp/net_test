#!/usr/bin/python

#60kb/s
import socket
import threading
import time
import random

CONNECTING = True
current_tick = 0
recv_length = 0
class ThreadClass(threading.Thread):
    def __init__(self, sock):
        self.sock = sock
        threading.Thread.__init__(self)
    def run(self):
        global current_tick
        global recv_length
        remain = ""
        last_msg = ""
        msg = ""
        while  CONNECTING:
            last_msg = msg
            msg = self.sock.recv(1024)
            if msg == "":
                continue
            if time.time() - current_tick < 1:
                recv_length += len(msg)
                continue
            current_tick = time.time()
            print "recv_len:%.2fKB" % (float(recv_length) / 1024)
            recv_length = 0



sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("123.58.171.152", 8890))

s = ThreadClass(sock)
s.start()

try:
  while True:
      send_msg = ""
      for i in range(random.randint(1, 100)):
          send_msg += "%s"%(i%10)
      send_msg += "\n"
      sock.send("%s:%s"%(time.clock(), send_msg))
      time.sleep(0.01)
except Exception:
  CONNECTING = False

