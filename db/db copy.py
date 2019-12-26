# 查终端记录数据库，标记网卡类型，查询终端用户表，将记录写入 csv

import model
import pymongo
import re
import copy
import judge

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_terminal = db.terminal
collection_users = db.users

l = []
ip = re.compile(r"IP:((\d+.){3}(\d+))")
netcard = re.compile(r"] (.+) IP:")

# result_target = db.target.find({"uname":"liyong130"})
result_target = db.target.find({"sizeOfip_local":{'$gte':2}})#.limit(50)

# 遍历多 ip 终端，为终端网卡类型打标
for doc in result_target:
    adapter_ip = copy.deepcopy(model.adapter_type)
    ip_list = []
    # print(doc)
    for adapter in doc["ip_local"]:
        # print(adapter)
        if ip.search(adapter):
            device_ip = ip.search(adapter).group(1)
            if(device_ip == "0.0.0.0"):
                continue
            ip_list.append(device_ip)

            adaptermodel = netcard.findall(adapter)[0]
            adaptertype = model.march_device(adaptermodel)
            adapter_ip[adaptertype].append(device_ip)

    doc["ip_count"] = len(set(ip_list))
    # print(adapter_ip)
    doc["adapter_ip"] = adapter_ip
    # 查询用户表，匹配终端使用者信息
    user_info = db.users.find({"uname":doc["uname"]})
    
    try:
        doc["user_info"] = user_info[0]
    except:
        doc["user_info"] = {'_id': 'USER NOT FOUND', 'uname': 'USER NOT FOUND', 'name': 'USER NOT FOUND', 'mail': 'USER NOT FOUND', 'department': 'USER NOT FOUND', 'city': 'USER NOT FOUND'}

    l.append(doc)
    # print(adapter_ip)

with open(r"/home/yur/code/networkSecurity/db/报表1226.csv", "a", encoding="utf8") as sf:
    # 写入 csv 首行
    s = ", "
    titlelist = [
        "uname", 
        "city", 
        "name", 
        "department",
        "system",
        "ip_server", 
        "ip_count", 
        "adapter_ip",
        "judge"
    ]
    titlestr = s.join(titlelist)
    sf.write(titlestr + "\n")

    # 将字典逐个写入 csv
    for a in l:
        print(a["adapter_ip"])

        # if(a["ip_count"] < 2):
        #     continue

        ipl = []
        for key in a["adapter_ip"]:
            ips = "+".join(a["adapter_ip"][key])
            if ips:
                ipl.append(key + ":" + ips)
        adapter_ips = " ".join(ipl)
        print(adapter_ips)

        judgestr = judge.judge(a["adapter_ip"])
        # if("133." in adapter_ips) and ("10." in adapter_ips):
        #     judgestr += ("疑似双网卡 ")

        linelist = [
            a["uname"],
            a["user_info"]["city"],
            a["user_info"]["name"],
            a["user_info"]["department"],
            a["system"],
            a["ip_server"],
            str(a["ip_count"]),
            adapter_ips,
            judgestr
        ]
        

        linestr = s.join(linelist)
        sf.write(linestr + "\n")