import enet
import time

SHUTDOWN_MSG = "SHUTDOWN"

host = enet.Host(enet.Address(b"0.0.0.0", 54301), 10, 0, 0, 0)

send_msg = ""

def GetCurrentTime():
  return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

for i in range(2000):
  send_msg += str(i % 10) 

send_index = 0 

send_count = 0 

connect_count = 0 
run = True
shutdown_recv = False
while run:
    # Wait 1 second for an event
    event = host.service(1000)
    if event.type == enet.EVENT_TYPE_CONNECT:
        send_index = 0 
        print("[%s]%s: CONNECT" % (GetCurrentTime(), event.peer.address, ))
        connect_count += 1
    elif event.type == enet.EVENT_TYPE_DISCONNECT:
        print("[%s]%s: DISCONNECT" % (GetCurrentTime(), event.peer.address))
        connect_count -= 1
        if connect_count <= 0 and shutdown_recv:
          run = False
    elif event.type == enet.EVENT_TYPE_RECEIVE:
        #print("%s: IN:  %r" % (event.peer.address, event.packet.data))
        msg = event.packet.data
        #print msg
        send_count += 1
        send_index += 1
        #print send_index
        send_data = "%10d%s"%(int(msg[:10]), send_msg)
        for i in range(10):
          if event.peer.send(0, enet.Packet(send_data, enet.PACKET_FLAG_RELIABLE)) < 0:
            print("%s: Error sending echo packet!" % event.peer.address)
        if event.packet.data == "SHUTDOWN":
          shutdown_recv = True

