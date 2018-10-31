#!/usr/bin/env python

import sys
import pq_module as pq
import pq_comms as pqc

def process_frame(packet):
    print "Hello from ", packet['Source']

TCP_IP = '127.0.0.1'
TCP_PORT = 10000
BUFFER_SIZE = 1024

fname = sys.argv[1]

pq_class = pqc.pq(TCP_IP, TCP_PORT, BUFFER_SIZE, fname, 10)

while 1:

    packets, data = pq_class.get_packet()

    #if not packets:
    for packet in packets:
        process_frame(packet)
