from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

data_mw = pd.read_csv('./weather_data\\mw.csv', encoding='gbk', header=0)
# city = ['德州', '济南', '聊城', '菏泽', '济宁', '泰安', '莱芜', '枣庄', '临沂', '日照', '淄博', '滨州', '东营', '潍坊',
#         '青岛', '烟台', '威海']


def get_data(path):
    path_1d = './weather_data\\' + str(path) + '1.csv'
    data_1d = pd.read_csv(path_1d, encoding='gbk', header=0)
    path_14d = './weather_data\\' + str(path) + '14.csv'
    data_14d = pd.read_csv(path_14d, encoding='gbk', header=0)
    return data_1d, data_14d


@app.route('/')
def home():
    return render_template('index.html', data_min=data_mw['最低温'].values.tolist(),
                           data_max=data_mw['最高温'].values.tolist())


@app.route('/index')
def index():
    return render_template('index.html', data_min=data_mw['最低温'].values.tolist(),
                           data_max=data_mw['最高温'].values.tolist())


@app.route('/dezhou')
def dezhou():
    data_1d, data_14d = get_data('德州')
    return render_template('city.html', city_name='德州', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/jinan')
def jinan():
    data_1d, data_14d = get_data('济南')
    return render_template('city.html', city_name='济南', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/liaocheng')
def liaocheng():
    data_1d, data_14d = get_data('聊城')
    return render_template('city.html', city_name='聊城', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/jining')
def jining():
    data_1d, data_14d = get_data('济宁')
    return render_template('city.html', city_name='济宁', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/weifang')
def weifang():
    data_1d, data_14d = get_data('潍坊')
    return render_template('city.html', city_name='潍坊', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/heze')
def heze():
    data_1d, data_14d = get_data('菏泽')
    return render_template('city.html', city_name='菏泽', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/yantai')
def yantai():
    data_1d, data_14d = get_data('烟台')
    return render_template('city.html', city_name='烟台', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


# @app.route('/laiwu')
# def laiwu():
#     data_1d, data_14d = get_data('莱芜')
#     return render_template('city.html', city_name='莱芜', time_1d=data_1d['小时'].values.tolist(),
#                            temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
#                            jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
#                            air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
#                            temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
#                            time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
#                            fangxiang1_14d=data_14d['风向1'].values.tolist(),
#                            fengxiang2_14d=data_14d['风向2'].values.tolist(),
#                            fengji_14d=data_14d['风级'].values.tolist())


@app.route('/weihai')
def weihai():
    data_1d, data_14d = get_data('威海')
    return render_template('city.html', city_name='威海', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/qingdao')
def qingdao():
    data_1d, data_14d = get_data('青岛')
    return render_template('city.html', city_name='青岛', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/rizhao')
def rizhao():
    data_1d, data_14d = get_data('日照')
    return render_template('city.html', city_name='日照', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/dongying')
def dongying():
    data_1d, data_14d = get_data('东营')
    return render_template('city.html', city_name='东营', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/zaozhuang')
def zaozhuang():
    data_1d, data_14d = get_data('枣庄')
    return render_template('city.html', city_name='枣庄', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/linyi')
def linyi():
    data_1d, data_14d = get_data('临沂')
    return render_template('city.html', city_name='临沂', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/zibo')
def zibo():
    data_1d, data_14d = get_data('淄博')
    return render_template('city.html', city_name='淄博', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/taian')
def taian():
    data_1d, data_14d = get_data('泰安')
    return render_template('city.html', city_name='泰安', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


@app.route('/binzhou')
def binzhou():
    data_1d, data_14d = get_data('滨州')
    return render_template('city.html', city_name='滨州', time_1d=data_1d['小时'].values.tolist(),
                           temp_1d=data_1d['温度'].values.tolist(), fengji_1d=data_1d['风级'].values.tolist(),
                           jiangshui_1d=data_1d['降水量'].values.tolist(), shidu_1d=data_1d['相对湿度'].values.tolist(),
                           air_1d=data_1d['空气质量'].values.tolist(), fangxiang_1d=data_1d['风力方向'].values.tolist(),
                           temp_min=data_14d['最低气温'].values.tolist(), temp_max=data_14d['最高气温'].values.tolist(),
                           time_14d=data_14d['日期'].values.tolist(), tianqi_14d=data_14d['天气'].values.tolist(),
                           fangxiang1_14d=data_14d['风向1'].values.tolist(),
                           fengxiang2_14d=data_14d['风向2'].values.tolist(),
                           fengji_14d=data_14d['风级'].values.tolist())


if __name__ == '__main__':
    app.run()
