#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import select
import Queue
import time
import os


import glVariable
import dataParse

dataParse = dataParse.dataParse()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ("0.0.0.0", 14567)
server.bind(server_address)
server.listen(10)

inputs = [server]
outputs = []
#message_queues = {}

print ("begining")
print (glVariable.seqNum)
glVariable.seqNum += 1
print (glVariable.seqNum)


while 1:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs, 30)
    
    if not (readable or writeable or exceptional):
        print ("time out")
        continue
    
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print ("    connection from ", client_address)
            connection.setblocking(0)
            inputs.append(connection)
 #           message_queues[connection] = Queue.Queue()

        else:
            try:
                data = s.recv(1024)
            except socket.error, msg:
                print (socket.error,  msg, "/", socket.errno, "/", msg[0], msg[1])
                if socket.errno.ECONNRESET == msg[0]:
                    print ("this error is ECONNRESET")
            else:
                if data :
                    print (" received " , data , "from ",s.getpeername())
                    dataParse.parse(data)
                    try:
                        s.send(data)
                    except socket.errno, msg:
                        if socket.errno.EAGAIN == msg[0]:
                            if s not in outputs:
                                outputs.append(s)

                    #              message_queues[s].put(data)
                # Add output channel for response
                # if s not in outputs:
                #     outputs.append(s)
                else:
                #Interpret empty result as closed connection
                    print ("  closing", client_address)
                    if s in outputs :
                        print ("remove")
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                #清除队列信息
   #             del message_queues[s]

    for s in writeable:
        # try:
        #     next_msg = message_queues[s].get_nowait()
        # except Queue.Empty:
        #     print " " , s.getpeername() , 'queue empty'
        #     outputs.remove(s)
        # else:
        #     print " sending " , next_msg , " to ", s.getpeername()
        #     os.popen('sleep 5').read()
        #     s.send(next_msg)
        pass
    for s in exceptional:
        print (" exception condition on ", s.getpeername())
        #stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        #清除队列信息
        # del message_queues[s]