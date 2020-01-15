# db.judge.aggregate([{$group:{_id:"$city",total:{$sum:1}}}])
# db.judge.aggregate([{$group:{_id:"$judge",total:{$sum:1}}}])
# db.judge.aggregate([{$group:{_id:{uname:"$uname",judge:"$judge"},total:{$sum:1}}}])
# db.judge.find({"judge":{$all:["正常"]}})

import csv
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_judge = db.judge
judge_agg = [{"$group":{"_id":"$judge","total":{"$sum":1}}}]
city_agg = [{"$group":{"_id":"$city","total":{"$sum":1}}}]

judge_list = ["正常","跨域","多网卡","非法VPN"]
city_list = ["开封","三门峡","许昌","焦作","鹤壁","商丘","南阳","濮阳","平顶山","周口","洛阳","驻马店","信阳","新乡","安阳","漯河","济源","郑州","河南"]
headers = ["_id","uname","city","name","department","system","ip_server","ip_count","adapter_ip","judge"]
result = collection_judge.aggregate(pipeline=judge_agg)
d = {}

for r in result:
    d[str(r["_id"])] = r["total"]
print(d)

# def get_all_judge():
#     for j in judge_list:
#         result = collection_judge.find({"judge":{"$all":[j]}}).count()
#         print(result)

def get_city_csv():
    
    for city in city_list:
        l = []
        for j in judge_list:
            detail_result = collection_judge.find({"city":city,"judge":{"$all":[j]}})
            for r in detail_result:
                l.append(r)
        with open("%s.csv" % city, "w+") as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(l)
            print(city)

def get_city_judge():
    d = {}
    for city in city_list:
        d_city_judge = {}
        detail = {}
        # value = collection_judge.count_documents({"city":city})
        # 所有潜在风险终端数量，按照用户名去重，按照城市分类
        value = len(collection_judge.distinct("uname",{"city":city}))


        for j in judge_list:
            # detail_result = collection_judge.count_documents({"city":city,"judge":{"$all":[j]}})
            # 各类风险终端数量，按照用户名去重，按照城市分类
            detail_result = len(collection_judge.distinct("uname",{"city":city,"judge":{"$all":[j]}}))
            # d_city_judge["value"] = result
            detail[j] = detail_result

        d_city_judge["value"] = value
        d_city_judge["detail"] = detail
        d[city] = d_city_judge

    print(d)

if __name__ == "__main__":
    get_city_csv()
