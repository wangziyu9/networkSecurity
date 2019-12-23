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
netcard = re.compile(r"] (.+) IP")
l = []
result_target = db.target.find()
# 遍历多 ip 终端，用正则表达式为终端网卡类型打标
for r in result_target:
    # rd = copy.deepcopy(d)
    for net in r["ip_local"]:
        try:
            l.append(netcard.findall(net)[0])
        except:
            pass

print(set(l))