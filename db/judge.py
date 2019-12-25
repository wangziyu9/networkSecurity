import json
import re


oss = re.compile(r"256.")
mss = re.compile(r"10.5[6|7]")
bss = re.compile(r"133.")
personal = re.compile(r"(\d+.){3}(\d+)")
vpn = re.compile(r"10.((0)|(25[1,3])|(56)).")


def judge(d):
    judge = ""

    totalzone = 0
    zone = {
        "OSS":0,
        "MSS":0,
        "BSS":0,
        "个人网":0
    }
    for key, value in d.items():
        if d[key] == "VPN":
            continue
        for ip in d[key]:
            if(oss.search(ip)):
                zone["OSS"] = 1
            elif(mss.search(ip)):
                zone["MSS"] = 1
            elif(bss.search(ip)):
                zone["BSS"] = 1
            else:
                zone["个人网"] += 1

    for key, value in zone.items():
        if zone[key]:
            judge += key
            judge += " "
        totalzone += value

    if totalzone == 2:
        judge += "双网卡 "
    if totalzone > 2:
        judge += "多网卡 "

    illegalvpn = 0
    if d["unknownVPN"]:
        # judge += d["VPN"] 
        for ip in d["unknownVPN"]:
            if not vpn.search(ip):
                illegalvpn = 1
    if d["VPN"]:
        # judge += d["VPN"] 
        for ip in d["VPN"]:
            if not vpn.search(ip):
                illegalvpn = 1

    if illegalvpn:
        judge += "非法VPN"
    return(judge)

d = {'Ethernet': ['10.57.116.201'], 'Ethernet+External': [], 'Ethernet+Onboard': ['133.163.20.101', '10.57.116.201'], 'External': [], 'Onboard': [], 'Others': [], 'VPN': ['10.56.1.1'], 'VirtualAdapter': [], 'Wireless': [], 'Wireless+External': ['172.30.235.1'], 'Wireless+Onboard': [], 'unknownVPN': ['1.1.1.1']}
print(judge(d))
