
from scapy.layers.inet import IP,TCP
from scapy.sendrecv import sr

class XmasScan:

    def __init__(self, destination, ports):
        self.target=destination
        self.ports= ports
    def response_data(self, ans):
        for s,r in ans:
            print("Xmas packet send : ",s.summary())
            print("Xmas packet response : ",r.summary())
    def not_response_data(self, unans):
        for r in unans:
            print("Xmas not response : ",r.summary())
    def scan(self):
        return sr(IP(dst=self.target)/TCP(dport=self.ports,flags="FPU") , timeout=2)


def main():
    target = "192.168.1.63"
    ports=[]
    for i in range(65535):
        ports.append(i)
    xmas= XmasScan(target, ports)
    ans, unans = xmas.scan()
    xmas.response_data(ans)
    #xmas.not_response_data(unans)
    print("Not filtered ports : ", len(ans))
    print("Filtered ports : ", len(unans))


if __name__=="__main__":
    main()