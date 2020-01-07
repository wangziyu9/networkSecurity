import json
import re

henan_vpn = re.compile(r"10.59.253.22(8|9)")
national_vpn = re.compile(r"^10.253")
oss = re.compile(r"^256.")
mss = re.compile(r"^10.5[6|7]")
bss = re.compile(r"^133.")
personal = re.compile(r"^(\d+.){3}(\d+)")

vpn = re.compile(r"^(10.((0)|(25[1,3])|(56)).)|(133.160.)")
# 10.0 10.56 10.251/3 133.160


def judge(d):
    judge = []

    # 网络类型判断
    totalzone = 0
    zone = {
        "OSS":0,
        "MSS":0,
        "BSS":0,
        "个人网":0
    }
    for key, value in d.items():
        if key == "VPN" or key == "unknownVPN" or key == "VirtualAdapter":
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

    if totalzone >= 1:
        for key, value in zone.items():
            if zone[key]:
                judge.append(key)

        if totalzone == 2:
            judge.append("双网卡")
        if totalzone > 2:
            judge.append("多网卡")

    # VPN 类型判断
    illegalvpn = 0
    if d["unknownVPN"]:
        # judge.append(d["VPN"] )
        for ip in d["unknownVPN"]:
            if henan_vpn.search(ip):
                judge.append("河南VPN")
            elif national_vpn.search(ip):
                judge.append("集团VPN")
            else:
                illegalvpn = 1
    if d["VPN"]:
        # judge.append(d["VPN"] )
        for ip in d["VPN"]:
            if henan_vpn.search(ip):
                judge.append("河南VPN")
            elif national_vpn.search(ip):
                judge.append("集团VPN")
            else:
                illegalvpn = 1

    if illegalvpn:
        judge.append("非法VPN")

    if judge == "":
        judge.append("正常")

    return(judge)

# d = {'Ethernet': ['133.169.12.13'], 'Others': [], 'Wireless+External': [], 'unknownVPN': [], 'External': [], 'Onboard': [], 'Wireless': [], 'VPN': [], 'VirtualAdapter': [], 'Ethernet+External': [], 'Ethernet+Onboard': [], 'Wireless+Onboard': []}
# print(judge(d))
