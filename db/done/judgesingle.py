import json
import re

henan_vpn = re.compile(r"10.59.253.22(8|9)")

oss = re.compile(r"^256.")
mss = re.compile(r"^10.5[6|7]")
bss = re.compile(r"133.")
personal = re.compile(r"^(\d+.){3}(\d+)")

vpn = re.compile(r"^(10.((0)|(25[1,3])|(56)).)|(133.160.)")
# 10.0 10.56 10.251/3 133.160


def judge(server, local):
    judge = ""
    if mss.findall(server):
        if bss.findall(local):
            judge += "bss-mss跨域互访 "
        else:
            judge += "个人网访问mss，未捕获VPN "
    if henan_vpn.findall(server):
            judge += "个人网访问，未捕获henan_vpn "
    return(judge)

# d = {'Ethernet': [], 'Others': [], 'Wireless+External': [], 'unknownVPN': ['133.160.1.1'], 'External': [], 'Onboard': [], 'Wireless': [], 'VPN': ['10.251.1.84'], 'VirtualAdapter': [], 'Ethernet+External': [], 'Ethernet+Onboard': ['192.168.0.102'], 'Wireless+Onboard': []}
# print(judge(d))
