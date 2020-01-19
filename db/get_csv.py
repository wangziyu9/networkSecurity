import csv
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.TERMINAL
collection_judge = db.judge

judge_list = ["正常","跨域","多网卡","非法VPN"]
city_list = ["开封","三门峡","许昌","焦作","鹤壁","商丘","南阳","濮阳","平顶山","周口","洛阳","驻马店","信阳","新乡","安阳","漯河","济源","郑州","河南"]
headers = ["_id","uname","city","name","department","system","ip_server","ip_count","adapter_ip","judge"]

def get_city_csv():
    
    for city in city_list:
        l = []
        for judge_type in judge_list:
            # 按城市和类型从数据库取数据
            detail_result = collection_judge.find({"city":city,"judge":{"$all":[judge_type]}})
            for r in detail_result:
                l.append(r)

        with open("%s.csv" % city, "w+") as f:
            # 写 csv
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(l)
            print(city + " OK")

if __name__ == "__main__":
    get_city_csv()
