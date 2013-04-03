#!/usr/bin/python

#60kb/s
import socket
import threading
import time
import random

CONNECTING = True
class ThreadClass(threading.Thread):
    def __init__(self, sock):
        self.sock = sock
        threading.Thread.__init__(self)
    def run(self):
        remain = ""
        last_msg = ""
        msg = ""
        while  CONNECTING:
            last_msg = msg
            msg = self.sock.recv(1024)
            if msg == "":
                continue
            recv_msgs = msg.split("\n")
            if len(recv_msgs) == 0:
                continue
            #    check_str = getdata[1]
            #    for i in range(len(check_str)):
            #        if check_str[i] != "%s"%(i%10):
            #            raise 'BIG ERROR. UNKNOWN'


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("123.58.171.152", 8888))

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

