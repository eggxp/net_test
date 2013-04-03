#!/usr/bin/python
import socket
import threading

class ThreadClass(threading.Thread):
    def __init__(self, sock):
        self.sock = sock
        threading.Thread.__init__(self)
    def run(self):
        remain = ""
        last_msg = ""
        msg = ""
        while True:
            last_msg = msg 
            msg = self.sock.recv(1024)
            if msg == "": 
                continue
            recv_msgs = msg.split("\n")
            if len(recv_msgs) == 0:
                continue
            recv_msgs[0] = remain + recv_msgs[0]
            if msg[len(msg)-1] != '\n':
                remain = recv_msgs[len(recv_msgs) - 1]
            else:
                remain = ""
            del recv_msgs[len(recv_msgs) - 1]
            send_data = ""
            for spmsg in recv_msgs:
                getdata = spmsg.split(":")
                send_data += "%s"%getdata[0]
                for x in range(10):
                    send_data += "%s"%getdata[1]
                send_data += "\n"
            self.sock.send(send_data)
    
a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a.bind(("0.0.0.0",8888))
a.listen(1)
while(1):
    cs,ca=a.accept()
    thread = ThreadClass(cs)
    thread.start()
    print ca

