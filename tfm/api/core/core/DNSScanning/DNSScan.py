from scapy.all import *

class DNSScan():

    def __init__(self, target_dns,  target_ip):
        self.target_ip = target_ip
        self.target=target_dns


    def get_data(self, ans, qtype, output):
        if qtype == "A":
            if ans and ans.an:
                ip = ans.an.rdata
                output.append(str(ip))
        elif qtype == "SOA":
            if ans and ans.ns :
                rrname = ans.ns.rrname
                if rrname :
                    rrname = rrname.decode("UTF8")
                    print("Request SOA rrname: ", rrname)
                rname = ans.ns.rname
                if rname :
                    rname = rname.decode("UTF-8")
                    print("Request SOA rrname: ", rname)
                mname = ans.ns.mname
                if mname:
                    mname = mname.decode("UTF-8")
                    print("Request SOA rrname: ", mname)
                output.append([rrname, rname, mname])
        elif qtype == "MX":
            results=[]
            if ans and ans.an:
                for x in ans.an.iterpayloads():
                    print(x.show())
                    if "exchange" in [x.show()]:
                        results.append(x.exchange.decode("UTF-8"))
            print("Request MX results: ", results)
            output.append(results)
        return output


    def do_scan(self):
        output=[]
        for qtype in ["A", "SOA", "MX"]:
            output = self.get_data(sr1(IP(dst=self.target)/UDP(sport=RandShort(), dport=53)
                            /DNS(rd=1, qd=DNSQR(qname=self.target_ip, qtype=qtype)),timeout=2), qtype, output)
        print("Final output : ", output)
        return output



def main():

    ###DNS Request
    dns = DNSScan("8.8.8.8", "aula.campusciberseguridad.com")
    ans = dns.do_scan()


if __name__ == "__main__":
    main()