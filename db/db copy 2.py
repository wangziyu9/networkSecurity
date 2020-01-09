# 查终端记录数据库，标记网卡类型，查询终端用户表，将记录写入 csv

import model
import pymongo
import re
import copy
import judge
from pandas import read_csv;

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_terminal = db.terminal
collection_users = db.users
collection_judge = db.judge

file_name = r"/home/yur/code/networkSecurity/db/报表0107.csv"
with open(file_name, "a", encoding="utf8") as sf:
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

l = []
ip = re.compile(r"IP:((\d+.){3}(\d+))")
netcard = re.compile(r"] (.+) IP:")

# result_target = db.target.find({"uname":"15639107968"},no_cursor_timeout=True)
# result_targe
# t = db.target.find({"uname":{'$regex':}).skip(29000) ##.limit(50)#
# result_target = db.target.find({"sizeOfip_local":{'$gte':2}},no_cursor_timeout=True)#.skip(29000) ##.limit(50)#
result_target = db.target.find({"sizeOfip_local":{'$gte':2}},no_cursor_timeout=True)#.limit(300)#
# 未采集到 iplocal

# 遍历多 ip 终端，为终端网卡类型打标
for doc in result_target:
    adapter_ip = copy.deepcopy(model.adapter_type)
    ip_list = []
    # print(doc)
    for adapter in doc["ip_local"]:
        # 通过网卡名称和 ip，判断网卡类型和对应的 ip
        if ip.search(adapter):
            device_ip = ip.search(adapter).group(1)
            if(device_ip == "0.0.0.0"):
                continue
            ip_list.append(device_ip)

            adaptermodel = netcard.findall(adapter)[0]
            adaptertype = model.march_device(adaptermodel)
            adapter_ip[adaptertype].append(device_ip)

    doc["adapter_ip"] = adapter_ip

    # 所有 Iplocal 中不重复的 Ip 数量
    doc["ip_count"] = len(set(ip_list))
    
    # 查询用户表，匹配终端使用者信息
    user_info = db.users.find({"uname":doc["uname"]},no_cursor_timeout=True)
    
    try:
        doc["user_info"] = user_info[0]
    except:
        doc["user_info"] = {'_id': 'USER NOT FOUND', 'uname': 'USER NOT FOUND', 'name': 'USER NOT FOUND', 'mail': 'USER NOT FOUND', 'department': 'USER NOT FOUND', 'city': 'USER NOT FOUND'}
    user_info.close()
    # l.append(doc)
    # print(adapter_ip)

    # 将字典逐个写入 csv
    # print(doc["uname"])
    # print(doc["adapter_ip"])
    ipl = []
    for key in doc["adapter_ip"]:
        ips = "+".join(doc["adapter_ip"][key])
        if ips:
            ipl.append(key + ":" + ips)
    adapter_ips = " ".join(ipl)
    # print(adapter_ips)
    # 调用判断是否违规
    judgelst = judge.judge(doc["adapter_ip"])

    # linelist = [
    #     doc["uname"],
    #     doc["user_info"]["city"],
    #     doc["user_info"]["name"],
    #     doc["user_info"]["department"],
    #     doc["system"],
    #     doc["ip_server"],
    #     str(doc["ip_count"]),
    #     adapter_ips,
    #     str(judgelst)
    # ]

    d = {
        "uname":doc["uname"], 
        "city":doc["user_info"]["city"], 
        "name":doc["user_info"]["name"], 
        "department":doc["user_info"]["department"],
        "system":doc["system"],
        "ip_server":doc["ip_server"], 
        "ip_count":str(doc["ip_count"]), 
        "adapter_ip":adapter_ips,
        "judge":judgelst    
    }
    collection_judge.insert_one(d)
    # linestr = s.join(linelist)
    # with open(file_name, "a", encoding="utf8") as sf:
    #     sf.write(linestr + "\n")

# result_target.close()
# df = read_csv(file_name)
# newDF = df.drop_duplicates()
# newDF.to_csv(file_name)