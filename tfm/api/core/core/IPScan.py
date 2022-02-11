#!/usr/bin/python3

from scapy.all import *
from scapy.sendrecv import sr
from multiprocessing.pool import ThreadPool


class IPScan:
    def __init__(self, target, init, end, ports):
        self.target = target
        self.init= init
        self.end = end
        self.ports = ports

    def scan(self):
        return sr(IP(dst=self.target, proto=(self.init, self.end)) / TCP(sport=44555, dport=self.ports), timeout=1)

    def response_data(self, ans):
        output=[]
        for s,r in ans:
            #print("r.summary() ", r.summary())
            val = str(r.summary())
            #print(val)
            if "SA" in val:
                #print(r[1]["TCP"][0].show())
                output.append(r[1]["TCP"][0].show())
        return output


def main():
    ports = []
    for i in range(500):
        ports.append(i)
    # define worker function before a Pool is instantiated
    def worker(ports):
        ip = IPScan("192.168.1.22", 0, 250, ports)
        ans, unans = ip.scan()
        return ip.response_data(ans)

    def next(ports, count):
        return ports[count]

    class ThreadWithReturnValue(Thread):
        def __init__(self, group=None, target=None, name=None,
                     args=(), kwargs={}, Verbose=None):
            Thread.__init__(self, group, target, name, args, kwargs)
            self._return = None

        def run(self):
            print(type(self._target))
            if self._target is not None:
                self._return = self._target(*self._args,**self._kwargs)

        def join(self, *args):
            Thread.join(self, *args)
            return self._return

    threads=[]
    threads= [0 for i in range(5)]
    count=0
    ports=[40,22,80,443,50]
    for i in ports:
        threads[count] = ThreadWithReturnValue(target=worker, args=(i,))
        threads[count].start()
        count+=1
    print("Launch all threads ")

    for i in range(len(threads)):
        if i < len(ports):
            print("Responses : ", threads[i].join())

    #pool = ThreadPool(processes=20)
    #response = []
    #for port in [1, 22, 80]:
    #    pool.apply_async(worker, (port,))
    #    res = pool.apply_async(os.getpid, ())
    #    print("Port ", port , "res ", res)
    #    response.append(res.get())

    #print("All Threads launched : ", response)

    #for i in response:
    #    print("result ", res, " : ",  res.get(timeout=1))
    #pool.close()
    #pool.join()




if __name__=="__main__":
    main()