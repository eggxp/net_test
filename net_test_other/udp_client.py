#!/usr/bin/python
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
        readmsg = ''
        while True:
          try:
            tmp, addr = sock.recvfrom(1024)
            if not tmp:
              continue
            readmsg += tmp
            if tmp.endswith('#'):
              break
          except:
            break
        cur_tick = time.clock()
        readlist = readmsg.split(':')
        if len(readlist) > 2 and len(readlist[2]) == 50 * 10 * 10 + 1:
          if readlist[2] != recv_msg:
            print 'error', readlist[0]
          else:
            tick = float(readlist[1])
            print 'ping:', (cur_tick - tick) * 1000, readlist[0]
        else:
          print 'error'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a = ThreadClass(sock)
a.start()
cnt = 0
while True:
  sendmsg = '%s:%s:%s' % (cnt, time.clock(), send_msg)
  sock.sendto(sendmsg, ('192.168.11.97', 8888))
  #sock.sendto(sendmsg, ('123.58.171.152', 8889))
  cnt += 1
  time.sleep(1)

