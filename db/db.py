# 查终端记录数据库，标记网卡类型，查询终端用户表，将记录写入 csv

import pymongo
import re
import copy

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_terminal = db.terminal
collection_users = db.users

# 网卡类型字典表
d = {
    "Wireless":"",
    "Ethernet":"",
    "VPN":"",
    "USB":"",
    "PCI":""
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
    rd = copy.deepcopy(d)
    ip_list = []
    # print(r)
    for adapter in r["ip_local"]:
        # print(adapter)
        if pci.search(adapter):
            rd["PCI"] = ip.search(adapter).group(1)
        elif usb.search(adapter):
            rd["USB"] = ip.search(adapter).group(1)
        elif vpn.search(adapter):
            rd["VPN"] = ip.search(adapter).group(1)
        
        if wireless.search(adapter):
            rd["Wireless"] = ip.search(adapter).group(1)
        elif ethernet.search(adapter):
            rd["Ethernet"] = ip.search(adapter).group(1)
    for key, value in rd.items():
        if(value):
            ip_list.append(value)

    # 将网卡标记添加进字典
    r["status"] = rd
    # ip 数量
    r["ip_count"] = len(set(ip_list))
    
    # 查询用户表，匹配终端使用者信息
    user_info = db.users.find({"uname":r["uname"]})
    if user_info:
        r["user_info"] = user_info[0]
    
    
    l.append(r)
    # print(rd)

with open(r"/home/yur/code/networkSecurity/db/terminal.csv", "a", encoding="utf8") as sf:
    # 写入 csv 首行
    sf.write("uname, city, name, ip_server, ip_count, Ethernet, Wireless, PCI, USB, VPN\n")

    # 将字典逐个写入 csv
    for a in l:
        line = ''
        line = line + a["uname"] + ", " + a["user_info"]["city"] + ", " + a["user_info"]["name"]
        line = line + ", " + a["ip_server"] + ", " + str(a["ip_count"])
        line = line + ", " + a["status"]["Ethernet"] + ", " + a["status"]["Wireless"] + ", " + a["status"]["PCI"] + ", " + a["status"]["USB"] + ", " + a["status"]["VPN"]
        sf.write(line + "\n")