# 查终端记录数据库，标记网卡类型，查询终端用户表，将记录写入 csv

import pymongo
import re
import copy
d = {'202.102.':0, '10.97.':0, '10.211.':0, '133.173.':0, '192.164.':0, '133.161.':0, '133.178.':0, '221.14.':0, '100.90.':0, '61.158.':0, '10.253.':0, '133.163.':0, '133.170.':0, '10.251.':0, '10.10.':0, '133.168.':0, '133.164.':0, '115.54.':0, '10.57.':0, '133.176.':0, '100.114.':0, '133.174.':0, '172.22.':0, '137.32.':0, '2.0.':0, '172.23.':0, '123.7.':0, '192.168.':0, '0.0.':0, '133.169.':0, '123.15.':0, '172.29.':0, '10.190.':0, '172.28.':0, '172.27.':0, '172.24.':0, '172.30.':0, '10.56.':0, '61.54.':0, '218.28.':0, '198.18.':0, '10.122.':0, '172.25.':0, '10.16.':0, '10.3.':0, '61.163.':0, '1.1.':0, '133.171.':0, '169.254.':0, '133.177.':0, '133.172.':0, '133.160.':0, '172.21.':0, '133.175.':0, '133.162.':0, '172.18.':0, '127.0.':0, '172.17.':0, '218.29.':0, '172.20.':0, '133.167.':0, '10.59.':0, '222.136.':0, '172.26.':0, '125.40.':0, '182.115.':0, '100.64.':0, '10.0.':0, '172.19.':0, '172.16.':0, '133.166.':0, '133.165.':0, '192.169.':0, '61.168.':0}
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL

netcard = re.compile(r"] (.+) IP:")
ip = re.compile(r"IP:((\d+.){3}(\d+))")
ip2 = re.compile(r"IP:((\d+.){2})")

ml = []
il = []
result_target = db.target.find()

# 遍历多 ip 终端
for r in result_target:
    for net in r["ip_local"]:
        try:
            d[ip2.search(net).group(1)] += 1
            ml.append(netcard.findall(net)[0])
        except:
            pass

with open(r"/home/yur/code/networkSecurity/db/iptable.txt", "a", encoding="utf8") as sf:
    sf.write(str(d))