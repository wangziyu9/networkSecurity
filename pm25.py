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
    l = db.get_data.get_henan_aqi_rank()
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
