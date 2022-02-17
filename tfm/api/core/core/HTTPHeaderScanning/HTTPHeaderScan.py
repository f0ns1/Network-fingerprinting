from scapy.all import *
from scapy.layers.http import *

class HTTPHeaderScan():

    def __init__(self,  target_ip, path, port=None):
        self.target_ip = target_ip
        self.path = path
        self.port=80
        if port:
            self.port=port

    def parse_output(self, response):
        output = []
        http_version = response[1].Http_Version
        if http_version:
            output.append(["http_version",http_version.decode("UTF-8")])
        status_code = response[1].Status_Code
        if status_code:
            output.append(["status_code", status_code.decode("UTF-8")])
        reason_pharse = response[1].Reason_Phrase
        if reason_pharse:
            output.append(["reason_pharse", reason_pharse.decode("UTF-8")])
        cache_control = response[1].Cache_Control
        if cache_control:
            output.append(["cache_control", cache_control.decode("UTF-8")])
        content_length = response[1].Content_Length
        if content_length:
            output.append(["content_length", content_length.decode("UTF-8")])
        date = response[1].Date
        if date:
            output.append(["date", date.decode("UTF-8")])
        expires = response[1].Expires
        if expires:
            output.append(["expires", expires.decode("UTF-8")])
        location = response[1].Location
        if location:
            output.append(["location", location.decode("UTF-8")])
        pragma = response[1].Pragma
        if pragma:
            output.append(["pragma", pragma.decode("UTF-8")])
        set_cookie = response[1].Set_Cookie
        if set_cookie:
            output.append(["set_cookie", set_cookie.decode("UTF-8")])
        unknown_headers = response[1].Unknown_Headers
        if unknown_headers:
            unk=[]
            for val in unknown_headers:
                unk.append(val.decode("UTF-8"))
            output.append(["Unknown_Headers",unk])
        return output

    def do_scan(self):
        output=[]
        try:
            response = http_request(self.target_ip, self.path, self.port)
            print(response[1].show())
            if response and response[1]:
                output = self.parse_output(response)
        except:
            output.append("host: %s at port: %s is unrechable " % (self.target_ip, str(self.port)))
            pass
        print(output)
        return output


def main():
    a = HTTPHeaderScan("www.linkedin.com", "/")
    value = a.do_scan()
    print(value)

if __name__=="__main__":
    main()