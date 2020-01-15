import flask
from flask import send_file, send_from_directory
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

@app.route("/")
def hello_world():
    return render_template("dashboard.html")

@app.route('/file/<cityname>.csv', methods=['GET', 'POST'])
def download_csv(cityname):
    return send_file("./files/%s.csv" % cityname)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route("/data/dashboard_detial", methods=['GET', 'POST'])
def dashboard_detial_data():
    jsn_data = {'开封': {'value': 125, 'detail': {'正常': 76, '跨域': 12, '多网卡': 35, '非法VPN': 1}}, '三门峡': {'value': 117, 'detail': {'正常': 102, '跨域': 0, '多网卡': 9, '非法VPN': 0}}, '许昌': {'value': 137, 'detail': {'正常': 115, '跨域': 0, '多网卡': 14, '非法VPN': 5}}, '焦作': {'value': 145, 'detail': {'正常': 82, '跨域': 24, '多网卡': 51, '非法VPN': 0}}, '鹤壁': {'value': 77, 'detail': {'正常': 60, '跨域': 9, '多网卡': 18, '非法VPN': 0}}, '商丘': {'value': 83, 'detail': {'正常': 72, '跨域': 2, '多网卡': 10, '非法VPN': 0}}, '南阳': {'value': 199, 'detail': {'正常': 134, '跨域': 18, '多网卡': 47, '非法VPN': 15}}, '濮阳': {'value': 109, 'detail': {'正常': 65, '跨域': 25, '多网卡': 40, '非法VPN': 1}}, '平顶山': {'value': 155, 'detail': {'正常': 103, '跨域': 32, '多网卡': 59, '非法VPN': 2}}, '周口': {'value': 175, 'detail': {'正常': 100, '跨域': 46, '多网卡': 78, '非法VPN': 0}}, '洛阳': {'value': 279, 'detail': {'正常': 215, '跨域': 27, '多网卡': 49, '非法VPN': 3}}, '驻马店': {'value': 225, 'detail': {'正常': 196, '跨域': 20, '多网卡': 31, '非法VPN': 5}}, '信阳': {'value': 191, 'detail': {'正常': 43, '跨域': 26, '多网卡': 115, '非法VPN': 52}}, '新乡': {'value': 192, 'detail': {'正常': 119, '跨域': 50, '多网卡': 84, '非法VPN': 9}}, '安阳': {'value': 122, 'detail': {'正常': 106, '跨域': 0, '多网卡': 11, '非法VPN': 0}}, '漯河': {'value': 96, 'detail': {'正常': 85, '跨域': 1, '多网卡': 11, '非法VPN': 0}}, '济源': {'value': 41, 'detail': {'正常': 40, '跨域': 0, '多网卡': 2, '非法VPN': 0}}, '郑州': {'value': 370, 'detail': {'正常': 185, '跨域': 114, '多网卡': 200, '非法VPN': 3}}, '河南': {'value': 172, 'detail': {'正常': 15, '跨域': 1, '多网卡': 71, '非法VPN': 19}}}
    detial_data = []
    for key in jsn_data:
        d = {}
        d["0.城市"] = key
        d["1.记录总量"] = jsn_data[key]["value"]
        d["2.跨域"] = jsn_data[key]["detail"]["跨域"]
        d["3.多网卡"] = jsn_data[key]["detail"]["多网卡"]
        d["4.非法VPN"] = jsn_data[key]["detail"]["非法VPN"]
        persent = (jsn_data[key]["detail"]["跨域"] + jsn_data[key]["detail"]["多网卡"] + jsn_data[key]["detail"]["非法VPN"]) / jsn_data[key]["value"] * 100
        d["5.异常占比"] = str(round(persent,2)) + "%"
        d["详细记录"] = "file/%s.csv" %key 
        detial_data.append(d)
    print(detial_data)
    return jsonify(detial_data)

@app.route("/data/dashboard_chart", methods=['GET', 'POST'])
def dashboard_chart_data():
    jsn_data = {'开封': {'value': 125, 'detail': {'正常': 76, '跨域': 12, '多网卡': 35, '非法VPN': 1}}, '三门峡': {'value': 117, 'detail': {'正常': 102, '跨域': 0, '多网卡': 9, '非法VPN': 0}}, '许昌': {'value': 137, 'detail': {'正常': 115, '跨域': 0, '多网卡': 14, '非法VPN': 5}}, '焦作': {'value': 145, 'detail': {'正常': 82, '跨域': 24, '多网卡': 51, '非法VPN': 0}}, '鹤壁': {'value': 77, 'detail': {'正常': 60, '跨域': 9, '多网卡': 18, '非法VPN': 0}}, '商丘': {'value': 83, 'detail': {'正常': 72, '跨域': 2, '多网卡': 10, '非法VPN': 0}}, '南阳': {'value': 199, 'detail': {'正常': 134, '跨域': 18, '多网卡': 47, '非法VPN': 15}}, '濮阳': {'value': 109, 'detail': {'正常': 65, '跨域': 25, '多网卡': 40, '非法VPN': 1}}, '平顶山': {'value': 155, 'detail': {'正常': 103, '跨域': 32, '多网卡': 59, '非法VPN': 2}}, '周口': {'value': 175, 'detail': {'正常': 100, '跨域': 46, '多网卡': 78, '非法VPN': 0}}, '洛阳': {'value': 279, 'detail': {'正常': 215, '跨域': 27, '多网卡': 49, '非法VPN': 3}}, '驻马店': {'value': 225, 'detail': {'正常': 196, '跨域': 20, '多网卡': 31, '非法VPN': 5}}, '信阳': {'value': 191, 'detail': {'正常': 43, '跨域': 26, '多网卡': 115, '非法VPN': 52}}, '新乡': {'value': 192, 'detail': {'正常': 119, '跨域': 50, '多网卡': 84, '非法VPN': 9}}, '安阳': {'value': 122, 'detail': {'正常': 106, '跨域': 0, '多网卡': 11, '非法VPN': 0}}, '漯河': {'value': 96, 'detail': {'正常': 85, '跨域': 1, '多网卡': 11, '非法VPN': 0}}, '济源': {'value': 41, 'detail': {'正常': 40, '跨域': 0, '多网卡': 2, '非法VPN': 0}}, '郑州': {'value': 370, 'detail': {'正常': 185, '跨域': 114, '多网卡': 200, '非法VPN': 3}}, '河南': {'value': 172, 'detail': {'正常': 15, '跨域': 1, '多网卡': 71, '非法VPN': 19}}}
    chart_data = {"cities":[], '跨域':[],'多网卡':[],'非法VPN':[]}
    for key in jsn_data:
        chart_data["cities"].append(key)
        chart_data["跨域"].append(jsn_data[key]["detail"]["跨域"])
        chart_data["多网卡"].append(jsn_data[key]["detail"]["多网卡"])
        chart_data["非法VPN"].append(jsn_data[key]["detail"]["非法VPN"])
    print(chart_data)
    return jsonify(chart_data)

@app.route("/data/overview", methods=['GET', 'POST'])
def overview_data():
    cities = []
    jsn_data = {'开封': {'value': 125, 'detail': {'正常': 76, '跨域': 12, '多网卡': 35, '非法VPN': 1}}, '三门峡': {'value': 117, 'detail': {'正常': 102, '跨域': 0, '多网卡': 9, '非法VPN': 0}}, '许昌': {'value': 137, 'detail': {'正常': 115, '跨域': 0, '多网卡': 14, '非法VPN': 5}}, '焦作': {'value': 145, 'detail': {'正常': 82, '跨域': 24, '多网卡': 51, '非法VPN': 0}}, '鹤壁': {'value': 77, 'detail': {'正常': 60, '跨域': 9, '多网卡': 18, '非法VPN': 0}}, '商丘': {'value': 83, 'detail': {'正常': 72, '跨域': 2, '多网卡': 10, '非法VPN': 0}}, '南阳': {'value': 199, 'detail': {'正常': 134, '跨域': 18, '多网卡': 47, '非法VPN': 15}}, '濮阳': {'value': 109, 'detail': {'正常': 65, '跨域': 25, '多网卡': 40, '非法VPN': 1}}, '平顶山': {'value': 155, 'detail': {'正常': 103, '跨域': 32, '多网卡': 59, '非法VPN': 2}}, '周口': {'value': 175, 'detail': {'正常': 100, '跨域': 46, '多网卡': 78, '非法VPN': 0}}, '洛阳': {'value': 279, 'detail': {'正常': 215, '跨域': 27, '多网卡': 49, '非法VPN': 3}}, '驻马店': {'value': 225, 'detail': {'正常': 196, '跨域': 20, '多网卡': 31, '非法VPN': 5}}, '信阳': {'value': 191, 'detail': {'正常': 43, '跨域': 26, '多网卡': 115, '非法VPN': 52}}, '新乡': {'value': 192, 'detail': {'正常': 119, '跨域': 50, '多网卡': 84, '非法VPN': 9}}, '安阳': {'value': 122, 'detail': {'正常': 106, '跨域': 0, '多网卡': 11, '非法VPN': 0}}, '漯河': {'value': 96, 'detail': {'正常': 85, '跨域': 1, '多网卡': 11, '非法VPN': 0}}, '济源': {'value': 41, 'detail': {'正常': 40, '跨域': 0, '多网卡': 2, '非法VPN': 0}}, '郑州': {'value': 370, 'detail': {'正常': 185, '跨域': 114, '多网卡': 200, '非法VPN': 3}}, '河南': {'value': 172, 'detail': {'正常': 15, '跨域': 1, '多网卡': 71, '非法VPN': 19}}}
    for key in jsn_data:
        cities.append(key)
    for c in cities:
        jsn_data[c + "市"] = jsn_data[c]
    return jsonify(jsn_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
