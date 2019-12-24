# 查终端记录数据库，标记网卡类型，查询终端用户表，将记录写入 csv

import pymongo
import re
import copy

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL

l = []
result_target = db.target.find()

# 遍历多 ip 终端
for r in result_target:
    for net in r["ip_local"]:
        try:
            l.append(netcard.findall(net)[0])
        except:
            pass

print(set(l))