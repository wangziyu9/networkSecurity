# 查终端记录数据库，标记网卡类型，查询终端用户表，将记录写入 csv

import model
import pymongo
import re
import copy
import judgesingle
from pandas import read_csv;

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_terminal = db.terminal
collection_users = db.users
result_target = db.target.find({"sizeOfip_local":{'$lte':1}},no_cursor_timeout=True)#.limit(50000)

d = {'公文系统': 0, '流程管控': 0, '销管系统': 0, 'RM系统': 0}

file_name = r"/home/yur/code/networkSecurity/db/singleillegal.csv"
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

    for doc in result_target:
        # print(doc['system']) 


        if doc['sizeOfip_local'] == 1:
            if doc['ip_local'][0] == '' or doc['ip_local'][0] == 'undefined':
                d[doc['system']] += 1
#             elif doc['ip_server'] not in doc['ip_local'][0]:
#                 judgestr = judgesingle.judge(doc['ip_server'], doc['ip_local'][0])
#                 if judgestr == "":
#                     continue
#                 user_info = db.users.find({"uname":doc["uname"]},no_cursor_timeout=True)
#                 try:
#                     doc["user_info"] = user_info[0]
#                 except:
#                     doc["user_info"] = {'_id': 'USER NOT FOUND', 'uname': 'USER NOT FOUND', 'name': 'USER NOT FOUND', 'mail': 'USER NOT FOUND', 'department': 'USER NOT FOUND', 'city': 'USER NOT FOUND'}
#                 user_info.close()

#                 linelist = [
#                     doc["uname"],
#                     doc["user_info"]["city"],
#                     doc["user_info"]["name"],
#                     doc["user_info"]["department"],
#                     doc["system"],
#                     doc["ip_server"],
#                     "1",
#                     # str(doc["ip_count"]),
#                     str(doc['ip_local']),
#                     judgestr
#                 ]
#                 linestr = ",".join(linelist)
#                 sf.write(linestr + "\n")
                
# df = read_csv(file_name)
# newDF = df.drop_duplicates()
# newDF.to_csv(file_name)
print(d)