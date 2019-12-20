# 查终端记录数据库，标记网卡类型，查询终端用户表，将记录写入 csv

import pymongo
import re
import copy
x = 0
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_terminal = db.terminal
collection_users = db.users

# 网卡类型字典表
d = {
    "Wireless":[],
    "Ethernet":[],
    "VPN":[],
    "USB":[],
    "PCI":[],
    "OTHER":[]
}

# 正则表达式匹配网卡类型
pci = re.compile(r"PCI")
usb = re.compile(r"USB")
vpn = re.compile(r"VPN")
wireless = re.compile(r"(Wireless)")
ethernet = re.compile(r"(Ethernet|PCIe? (GBE|FE))")
ip = re.compile(r"IP:((\d+.){3}(\d+))")

l = []
result_target = db.target.find({"sizeOfip_local":{'$gte':2}})
# 遍历多 ip 终端，用正则表达式为终端网卡类型打标
for r in result_target:
    x+=1
    rd = copy.deepcopy(d)
    ip_list = []
    # print(r)
    for adapter in r["ip_local"]:
        # print(adapter)
        if ip.search(adapter):
            device_ip = ip.search(adapter).group(1)
            ip_list.append(device_ip)

            if pci.search(adapter):
                rd["PCI"].append(device_ip)
            elif usb.search(adapter):
                rd["USB"].append(device_ip)
            elif vpn.search(adapter):
                rd["VPN"].append(device_ip)
            else:
                rd["OTHER"].append(device_ip)
            
            if wireless.search(adapter):
                rd["Wireless"].append(device_ip)
            elif ethernet.search(adapter):
                rd["Ethernet"].append(device_ip)
            else:
                rd["OTHER"].append(device_ip)

    # ip 去重
    for key in rd.keys():
        s = "+"
        rd[key] = list(set(rd[key]))
        s = s.join(rd[key])
        rd[key] = s

    # 将网卡标记，ip 数量添加进字典
    r["status"] = rd
    r["ip_count"] = len(set(ip_list))
    
    # 查询用户表，匹配终端使用者信息
    user_info = db.users.find({"uname":r["uname"]})
    
    try:
        r["user_info"] = user_info[0]
    except:
        r["user_info"] = {"city":"NOT FOUND","name":"NOT FOUND"}

    l.append(r)
    # print(rd)

with open(r"/home/yur/code/networkSecurity/db/报表.csv", "a", encoding="utf8") as sf:
    # 写入 csv 首行
    s = ", "
    titlelist = [
        "uname", 
        "city", 
        "name", 
        "ip_server", 
        "ip_count", 
        "Ethernet", 
        "Wireless", 
        "PCI", 
        "USB", 
        "VPN",
        "OTHER",
        "judge"
    ]
    titlestr = s.join(titlelist)
    sf.write(titlestr + "\n")

    # 将字典逐个写入 csv
    for a in l:
        if(a["ip_count"] < 2):
            continue
        linelist = [
            a["uname"],
            a["user_info"]["city"],
            a["user_info"]["name"],
            a["ip_server"],
            str(a["ip_count"]),
            a["status"]["Ethernet"],
            a["status"]["Wireless"],
            a["status"]["PCI"],
            a["status"]["USB"],
            a["status"]["VPN"],
            a["status"]["OTHER"]
        ]
        if("." in a["status"]["PCI"]) and ("." in a["status"]["USB"]):
            linelist.append("疑似双网卡")
        linestr = s.join(linelist)
        sf.write(linestr + "\n")