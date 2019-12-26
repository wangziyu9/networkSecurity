import json
import re


oss = re.compile(r"256.")
mss = re.compile(r"10.5[6|7]")
bss = re.compile(r"133.")
personal = re.compile(r"(\d+.){3}(\d+)")
vpn = re.compile(r"10.((0)|(25[1,3])|(56)).")


def judge(d):
    judge = ""

    # 网络类型判断
    totalzone = 0
    zone = {
        "OSS":0,
        "MSS":0,
        "BSS":0,
        "个人网":0
    }
    for key, value in d.items():
        if key == "VPN" or key == "unknownVPN" :
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

    for value in zone.values():
        totalzone += value

    if totalzone > 1:
        for key, value in zone.items():
            if zone[key]:
                judge += key
                judge += " "

        if totalzone == 2:
            judge += "双网卡 "
        if totalzone > 2:
            judge += "多网卡 "

    # VPN 类型判断
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

    if judge == "":
        judge += "正常"

    return(judge)

# d = {'Ethernet': [], 'Others': [], 'Wireless+External': [], 'unknownVPN': [], 'External': [], 'Onboard': [], 'Wireless': [], 'VPN': ['10.251.1.84'], 'VirtualAdapter': [], 'Ethernet+External': [], 'Ethernet+Onboard': ['192.168.0.102'], 'Wireless+Onboard': []}
# print(judge(d))
