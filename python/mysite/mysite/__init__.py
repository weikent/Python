import os
print os.getcwd()

# import sys  
# sys.path.append(os.getcwd())

from mqtt import MQTTServer
import os
import socket

import threading

servername = 'mosquitto.org'




def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print '%d is open' % port
        return True
    except:
        print '%d is down' % port
        return False

if IsOpen(servername, 1883):
    print "1"
    write = threading.Thread(target=MQTTServer.start)
    write.setDaemon(True)
    write.start()
#    MQTTServer.start()
else:
    print "3"







if __name__ == '__main__':
    IsOpen(servername, 1883)
