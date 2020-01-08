# db.judge.aggregate([{$group:{_id:"$city",total:{$sum:1}}}])
# db.judge.aggregate([{$group:{_id:"$judge",total:{$sum:1}}}])
# db.judge.aggregate([{$group:{_id:{uname:"$uname",judge:"$judge"},total:{$sum:1}}}])
# db.judge.find({"judge":{$all:["正常"]}})

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_judge = db.judge
judge_agg = [{"$group":{"_id":"$judge","total":{"$sum":1}}}]
city_agg = [{"$group":{"_id":"$city","total":{"$sum":1}}}]

judge_list = ["正常","跨域","多网卡","非法VPN"]
city_list = ["开封","三门峡","许昌","焦作","鹤壁","商丘","南阳","濮阳","平顶山","周口","洛阳","驻马店","信阳","新乡","安阳","漯河","济源","郑州","河南"]

result = collection_judge.aggregate(pipeline=judge_agg)
d = {}

for r in result:
    d[str(r["_id"])] = r["total"]
    # print(r)
print(d)

def get_all_judge():
    for j in judge_list:
        result = collection_judge.find({"judge":{"$all":[j]}}).count()
        print(result)

def get_city_judge(city):
    d_city_judge = {}
    value = {}
    for j in judge_list:
        result = collection_judge.count_documents({"city":city,"judge":{"$all":[j]}})
        # d_city_judge["value"] = result
        value[j] = result

    d_city_judge["name"] = city
    d_city_judge["value"] = value

    print(d_city_judge)

if __name__ == "__main__":
    for c in city_list:
        get_city_judge(c)