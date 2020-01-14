import flask
from flask import send_file, send_from_directory
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

@app.route("/")
def hello_world():
    return render_template("dashboard.html")
@app.route("/resume")
def download_resume():
    return send_file("./files/resume.pdf")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route("/data/dashboard_chart", methods=['GET', 'POST'])
def dashboard_chart_data():
    jsn_data = {
        "cities": ['郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡', '焦作', '濮阳', '许昌', '漯河', '三门峡', '南阳', '商丘', '信阳', '周口', '驻马店', '济源'],
        '跨域' : [220, 182, 191, 234, 290, 330, 310, 220, 182, 191, 234, 290, 330, 310, 234, 290, 330, 310],
        '多网卡' : [220, 182, 191, 234, 290, 330, 310, 220, 182, 191, 234, 290, 330, 310, 234, 290, 330, 310],
        '非法VPN': [220, 182, 191, 234, 290, 330, 310, 220, 182, 191, 234, 290, 330, 310, 234, 290, 330, 310]
        }
    return jsonify(jsn_data)

@app.route("/data/dashboard", methods=['GET', 'POST'])
def dashboard_data():
    jsn_data = {'开封市': {'value': 1, 'detail': {'正常': 1191, '跨域': 596, '多网卡': 739, '非法VPN': 10}}, '三门峡市': {'value': 1612, 'detail': {'正常': 1506, '跨域': 0, '多网卡': 66, '非法VPN': 0}}, '许昌市': {'value': 2163, 'detail': {'正常': 2058, '跨域': 0, '多网卡': 83, '非法VPN': 5}}, '焦作市': {'value': 1888, 'detail': {'正常': 994, '跨域': 529, '多网卡': 818, '非法VPN': 0}}, '鹤壁市': {'value': 1557, 'detail': {'正常': 977, '跨域': 477, '多网卡': 578, '非法VPN': 0}}, '商丘市': {'value': 1225, 'detail': {'正常': 1060, '跨域': 10, '多网卡': 160, '非法VPN': 0}}, '南阳市': {'value': 2537, 'detail': {'正常': 1728, '跨域': 476, '多网卡': 684, '非法VPN': 72}}, '濮阳市': {'value': 1673, 'detail': {'正常': 857, '跨域': 513, '多网卡': 797, '非法VPN': 1}}, '平顶山市': {'value': 2309, 'detail': {'正常': 1292, '跨域': 698, '多网卡': 961, '非法VPN': 36}}, '周口市': {'value': 2684, 'detail': {'正常': 1444, '跨域': 879, '多网卡': 1163, '非法VPN': 0}}, '洛阳市': {'value': 4344, 'detail': {'正常': 3491, '跨域': 403, '多网卡': 640, '非法VPN': 20}}, '驻马店市': {'value': 2820, 'detail': {'正常': 2389, '跨域': 235, '多网卡': 307, '非法VPN': 69}}, '信阳市': {'value': 2999, 'detail': {'正常': 874, '跨域': 654, '多网卡': 1682, '非法VPN': 348}}, '新乡市': {'value': 7801, 'detail': {'正常': 3591, '跨域': 3076, '多网卡': 4017, '非法VPN': 85}}, '安阳市': {'value': 1595, 'detail': {'正常': 1527, '跨域': 0, '多网卡': 53, '非法VPN': 0}}, '漯河市': {'value': 927, 'detail': {'正常': 866, '跨域': 1, '多网卡': 60, '非法VPN': 0}}, '济源市': {'value': 433, 'detail': {'正常': 423, '跨域': 0, '多网卡': 3, '非法VPN': 0}}, '郑州市': {'value': 8951, 'detail': {'正常': 3155, '跨域': 3405, '多网卡': 5727, '非法VPN': 12}}, '河南市': {'value': 3991, 'detail': {'正常': 117, '跨域': 3, '多网卡': 1928, '非法VPN': 162}}}
    return jsonify(jsn_data)

@app.route("/data/overview", methods=['GET', 'POST'])
def overview_data():
    jsn_data = {'开封市': {'value': 1, 'detail': {'正常': 1191, '跨域': 596, '多网卡': 739, '非法VPN': 10}}, '三门峡市': {'value': 1612, 'detail': {'正常': 1506, '跨域': 0, '多网卡': 66, '非法VPN': 0}}, '许昌市': {'value': 2163, 'detail': {'正常': 2058, '跨域': 0, '多网卡': 83, '非法VPN': 5}}, '焦作市': {'value': 1888, 'detail': {'正常': 994, '跨域': 529, '多网卡': 818, '非法VPN': 0}}, '鹤壁市': {'value': 1557, 'detail': {'正常': 977, '跨域': 477, '多网卡': 578, '非法VPN': 0}}, '商丘市': {'value': 1225, 'detail': {'正常': 1060, '跨域': 10, '多网卡': 160, '非法VPN': 0}}, '南阳市': {'value': 2537, 'detail': {'正常': 1728, '跨域': 476, '多网卡': 684, '非法VPN': 72}}, '濮阳市': {'value': 1673, 'detail': {'正常': 857, '跨域': 513, '多网卡': 797, '非法VPN': 1}}, '平顶山市': {'value': 2309, 'detail': {'正常': 1292, '跨域': 698, '多网卡': 961, '非法VPN': 36}}, '周口市': {'value': 2684, 'detail': {'正常': 1444, '跨域': 879, '多网卡': 1163, '非法VPN': 0}}, '洛阳市': {'value': 4344, 'detail': {'正常': 3491, '跨域': 403, '多网卡': 640, '非法VPN': 20}}, '驻马店市': {'value': 2820, 'detail': {'正常': 2389, '跨域': 235, '多网卡': 307, '非法VPN': 69}}, '信阳市': {'value': 2999, 'detail': {'正常': 874, '跨域': 654, '多网卡': 1682, '非法VPN': 348}}, '新乡市': {'value': 7801, 'detail': {'正常': 3591, '跨域': 3076, '多网卡': 4017, '非法VPN': 85}}, '安阳市': {'value': 1595, 'detail': {'正常': 1527, '跨域': 0, '多网卡': 53, '非法VPN': 0}}, '漯河市': {'value': 927, 'detail': {'正常': 866, '跨域': 1, '多网卡': 60, '非法VPN': 0}}, '济源市': {'value': 433, 'detail': {'正常': 423, '跨域': 0, '多网卡': 3, '非法VPN': 0}}, '郑州市': {'value': 8951, 'detail': {'正常': 3155, '跨域': 3405, '多网卡': 5727, '非法VPN': 12}}, '河南市': {'value': 3991, 'detail': {'正常': 117, '跨域': 3, '多网卡': 1928, '非法VPN': 162}}}
    return jsonify(jsn_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
