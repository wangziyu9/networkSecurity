import pymongo
import re
import copy

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection = db.terminal

d = {
    "Wireless":"",
    "Ethernet":"",
    "VPN":"",
    "USB":"",
    "PCI":""
}

pci = re.compile(r"PCI")
usb = re.compile(r"USB")
vpn = re.compile(r"VPN")
wireless = re.compile(r"(Wireless)")
ethernet = re.compile(r"(Ethernet|PCIe? (GBE|FE))")
ip = re.compile(r"IP:((\d+.){3}(\d+))")

l = []
result_target = db.target.find({"sizeOfip_local":{'$gte':2}})
for r in result_target:
    rd = copy.deepcopy(d)
    ip_list = []
    print(r)
    for adapter in r["ip_local"]:
        print(adapter)
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
    r["ip_count"] = len(set(ip_list))
    r["status"] = rd
    l.append(r)
    # print(rd)

with open(r"/home/yur/code/networkSecurity/db/adapter1.txt", "a", encoding="utf8") as sf:
    for a in l:
        sf.write(str(a)+ "\n")