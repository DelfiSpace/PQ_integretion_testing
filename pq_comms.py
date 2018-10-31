import json
import socket
import time

class pq:

    def __init__(self, ip, port, buffer_size, fname, log_period):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.buf = ""
        self.buffer_size = buffer_size
        self.f = open(fname,'a')
        self.log_period = log_period
        self.time_prev=  time.time()
        self.time_new =  0

    def get_packet(self):
        data = self.s.recv(self.buffer_size)

        self.f.write(data)
        #print "received data:", data
        self.time_new =  time.time()
        if self.time_new - self.time_prev > self.log_period*60:
            print 'Still here', self.time_new
            self.time_prev = self.time_new
            self.f.flush()

        packets = []
        sps = data.splitlines(True)
        for sp in sps:
            self.buf += sp
            if "\n" in self.buf:
                packet = json.loads(self.buf)
                self.buf = ""
                packets.append(packet)

        return packets, data
