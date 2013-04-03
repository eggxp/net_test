import enet
import os
import time

SHUTDOWN_MSG = b"SHUTDOWN"
MSG_NUMBER = 10

host = enet.Host(None, 1, 0, 0, 0)
#peer = host.connect(enet.Address(b"123.58.173.152", 54301), 1)
peer = host.connect(enet.Address(b"192.168.10.246", 54301), 1)

def GetCurrentTime():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def GetCurrentTick():
    return int(time.clock() * 1000)

send_index = 0

recv_index = 0

counter = 0
run = True
msg = ""
for i in range(20):
    msg += str(i % 10)
not_receive_count = 0
while run:
    event = host.service(100)
    if event.type == enet.EVENT_TYPE_CONNECT:
        not_receive_count = 0
        send_index = 0
        print("[%s]%s: CONNECT" % (GetCurrentTime(), event.peer.address))
    elif event.type == enet.EVENT_TYPE_DISCONNECT:
        print("[%s]%s: DISCONNECT" % (GetCurrentTime(), event.peer.address))
        run = False
        continue
    elif event.type == enet.EVENT_TYPE_RECEIVE:
        recv_index += 1
        if recv_index % 30 != 0:
            continue
        not_receive_count = 0
        cur_tick = int(event.packet.data[:10])
        
        print GetCurrentTick() - cur_tick
        #if send_index % 30 == 0:
        #    print "recv:%s"%int(event.packet.data[:4])
        continue
    else:
        not_receive_count += 1
        #if not_receive_count > 10:
        #    print "[%s]LAG!!!!!!!!!!"%GetCurrentTime()
        #if not_receive_count % 30 == 0:
        #    host = enet.Host(None, 1, 0, 0, 0)
        #    peer = host.connect(enet.Address(b"123.58.173.152", 54301), 1)

    send_index += 1
    if send_index % 30 == 0:
        print "send:%s"%send_index
    send_data = "%10d%s"%(GetCurrentTick(), msg)
    packet = enet.Packet(send_data)
    peer.send(0, packet)

    counter += 1
