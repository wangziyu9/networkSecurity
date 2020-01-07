# db.judge.aggregate([{$group:{_id:"$city",total:{$sum:1}}}])
# db.judge.aggregate([{$group:{_id:"$judge",total:{$sum:1}}}])
# 
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_judge = db.judge
judge_total = [{"$group":{"_id":"$judge","total":{"$sum":1}}}]
city_total = [{"$group":{"_id":"$city","total":{"$sum":1}}}]

result = collection_judge.aggregate(pipeline=city_total)
d = {}
for r in result:
    d[r["_id"]] = r["total"]
    # print(r)
print(d)