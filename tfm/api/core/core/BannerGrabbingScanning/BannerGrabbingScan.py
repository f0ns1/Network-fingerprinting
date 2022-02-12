from scapy.all import *

class BannerGrabbingScan():

    def __init__(self, target_ip, ports):
        self.target_ip = target_ip
        self.ports=[21, 22, 24, 53, 80, 443, 3846]
        if ports:
            self.ports = ports

    def getBanner(self,ip, port):
        banner=[]
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("socket ", s, "IP ", ip, "port ", port)
            s.settimeout(6)
            result = s.connect_ex((ip, port))
            print("result ", result)
            if result == 0:
                ans = s.recv(1024)
                print(ans)
                print("Port {}: Open".format(port))
                print('found -> ip:', ip, 'port:', port, 'banner:', str(ans))
                answ = 'ip:', ip, 'port:', port, 'banner:', str(ans)
                banner.append(answ)
            else:
                answ = 'ip:', ip, 'port:', port, 'result', result
                banner.append(answ)
        except Exception as e:
            answ = 'ip:', ip, 'port:', port, 'result: OPEN|', e
            banner.append(answ)
            print('bad port', port, ', please try again...')
            pass
        s.close()
        return banner

    def do_scan(self):
        output=[]
        for port in self.ports:
            output.append(self.getBanner(self.target_ip, port))
        return output


def main():
    banner = BannerGrabbingScan("192.168.1.22",None)
    output = banner.do_scan()
    print("output : ", output)
if __name__ == '__main__':
    main()