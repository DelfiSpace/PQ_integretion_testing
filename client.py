#!/usr/bin/env python

import sys
import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

fname = sys.argv[1]
time_prev =  time.time()
time_new = 0

print "Starting", time_prev

f = open(fname,'a')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while 1:
    data = s.recv(BUFFER_SIZE)
    f.write(data)
    #print "received data:", data
    time_new =  time.time()
    if time_new - time_prev > 10*60:
        print 'Still here', time_new
        time_prev = time_new
        f.flush()

s.close()
f.close()
