# db.judge.aggregate([{$group:{_id:"$city",total:{$sum:1}}}])
# db.judge.aggregate([{$group:{_id:"$judge",total:{$sum:1}}}])
# db.judge.aggregate([{$group:{_id:{uname:"$uname",judge:"$judge"},total:{$sum:1}}}])
# db.judge.find({"judge":{$all:["正常"]}})

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_judge = db.judge
judge_total = [{"$group":{"_id":"$judge","total":{"$sum":1}}}]
city_total = [{"$group":{"_id":"$city","total":{"$sum":1}}}]

judge_list = ["正常","双网卡","非法VPN"]
city_list = ["开封","三门峡","许昌","焦作","鹤壁","商丘","南阳","濮阳","平顶山","周口","洛阳","驻马店","信阳","新乡","安阳","漯河","济源","郑州","河南"]
result = collection_judge.aggregate(pipeline=judge_total)
d = {}
for r in result:
    d[str(r["_id"])] = r["total"]
    # print(r)
print(d)

for j in judge_list:
    result = collection_judge.find({"judge":{"$all":[j]}}).count()
    print(result)

for c in city_list:
    for j in judge_list:
        result = collection_judge.find({"city":c,"judge":{"$all":[j]}}).count()
        print(c + j)
        print(result)
