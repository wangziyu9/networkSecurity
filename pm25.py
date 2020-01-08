import flask
from flask import Flask, render_template, request, jsonify
import threading
from multiprocessing import Process
# import db.get_data

app = Flask(__name__)
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

# @app.route('/test.html')
@app.route('/test/')
def test():
    return render_template("plantcity.html")

@app.route('/')
def hello_world():
    return render_template("plant.html")


@app.route('/provincemap/<provincename>')
def rtn_province_map(provincename):
    return render_template("provincemapcopy3.html",provincename=provincename)
    
@app.route('/citymap/<cityname>')
def rtn_city_map(cityname):
    return render_template("citymapcopy3.html",cityname=cityname)

@app.route('/data/province/<provincename>', methods=['GET', 'POST'])
def rtn_data_province_coord(provincename):
    province = provincename
    d = {}
    d["coord"] = db.get_data.get_province_map_coord(province)
    d["aqi"] = db.get_data.get_province_map_aqi(province)
    d["center"] = db.get_data.get_province_map_center(province)
    print(d)
    return jsonify(d)

@app.route('/data/city/<cityname>', methods=['GET', 'POST'])
def rtn_data_city_coord(cityname):
    city = cityname
    d = {}
    d["coord"] = db.get_data.get_city_map_coord(city)
    d["aqi"] = db.get_data.get_city_map_aqi(city)
    d["center"] = db.get_data.get_city_map_center(city)
    print(d)
    return jsonify(d)

@app.route('/data/now', methods=['GET', 'POST'])
def rtn_data_now():
    d = db.get_data.get_now()
    return jsonify(d)

@app.route('/data/henan_aqirank', methods=['GET', 'POST'])
def rtn_data_aqirank_henan():
    # l = {"开封": 1185, "三门峡": 905, "许昌": 1184, "焦作": 1079, "鹤壁": 834, "商丘": 621, "南阳": 1292, "濮阳": 834, "平顶山": 1246, "周口": 1544, "洛阳": 2278, "驻马店": 1443, "信阳": 1503, "新乡": 4344, "安阳": 850, "漯河": 522, "济源": 200, "郑州": 4659}
    l = [{"name":"开封市","value": 1185},
        {"name":"三门峡市","value": 905},
        {"name":"许昌市","value": 1184},
        {"name":"焦作市","value": 1079},
        {"name":"鹤壁市","value": 834},
        {"name":"商丘市","value": 621},
        {"name":"南阳市","value": 1292},
        {"name":"濮阳市","value": 834},
        {"name":"平顶山市","value": 1246},
        {"name":"周口市","value": 1544},
        {"name":"洛阳市","value": 2278},
        {"name":"驻马店市","value": 1443},
        {"name":"信阳市","value": 1503},
        {"name":"新乡市","value": 4344},
        {"name":"安阳市","value": 850},
        {"name":"漯河市","value": 522},
        {"name":"济源市","value": 0},
        {"name":"郑州市","value": 4659}]
    return jsonify(l)

@app.route('/data/china_aqirank_top', methods=['GET', 'POST'])
def rtn_data_aqirank_china_top():
    l = db.get_data.get_aqi_rank_china_top()
    return jsonify(l)

@app.route('/data/china_aqirank', methods=['GET', 'POST'])
def rtn_data_aqirank_china():
    l = db.get_data.get_aqi_rank_china()
    return jsonify(l)    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
