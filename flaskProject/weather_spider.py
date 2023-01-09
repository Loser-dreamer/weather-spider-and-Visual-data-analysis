# spider.py
import requests
from bs4 import BeautifulSoup
import csv
import json
from ua_info import ua_list  # 使用自定义的ua池
import random
import time
import os
import clean


class WeatherSpider(object):
    def __init__(self):
        # 初始化url属性
        self.url1 = 'http://www.weather.com.cn/weather/{}'
        self.url2 = 'http://www.weather.com.cn/weather15d/{}'
        self.url3 = 'https://weather.cma.cn/web/weather/{}'
        # 地区id
        self.weather_id_14 = {
            '德州': 101120401,
            '济南': 101120101,
            '聊城': 101121701,
            '菏泽': 101121001,
            '济宁': 101120701,
            '泰安': 101120801,
            '莱芜': 101121601,
            '枣庄': 101121401,
            '临沂': 101120901,
            '日照': 101121501,
            '淄博': 101120301,
            '滨州': 101121101,
            '东营': 101121201,
            '潍坊': 101120601,
            '青岛': 101120201,
            '烟台': 101120501,
            '威海': 101121301
        }
        self.weather_id_mw = {
            '德州': 54714,
            '济南': 54823,
            '聊城': 54806,
            '菏泽': 54906,
            '济宁': 54915,
            '泰安': 54827,
            '莱芜': 54828,
            '枣庄': 58024,
            '临沂': 54938,
            '日照': 54945,
            '淄博': 54830,
            '滨州': 54734,
            '东营': 54736,
            '潍坊': 54843,
            '青岛': 54857,
            '烟台': 54765,
            '威海': 54774
        }
        self.spider_id = 1

    def get_html(self, url):
        # 请求获得网页内容
        try:
            headers = {'User-Agent': random.choice(ua_list)}
            r = requests.get(url, headers=headers, timeout=30)
            r.raise_for_status()
            # 判断返回的Response类型状态是不是200,如果是200，将表示返回的内容是正确的，如果不是200，会产生一个HttpError的异常
            r.encoding = r.apparent_encoding
            print('访问成功--', self.spider_id)
            self.spider_id += 1
            return r.text
        except:
            print('访问错误')
            return ''

    def get_content_7d(self, html):
        # 处理得到有用信息保存数据文件
        bs = BeautifulSoup(html, 'html.parser')  # 创建BeautifulSoup对象
        body = bs.body

        # 处理当天的数据
        data_today = body.find_all('div', {'class': 'left-div'})
        text = data_today[2].find('script').string
        text = text[text.index('=') + 1:-2]  # 移除var,将其变为json数据
        jd = json.loads(text)
        today = jd['od']['od2']  # 找到当天的数据
        final_day = []  # 初始化一个列表保存数据
        count = 0
        for i in today:
            temp = []  # 临时存放数据
            if count <= 23:
                temp.append(i['od21'])  # 添加时间
                temp.append(i['od22'])  # 添加当前时刻温度
                temp.append(i['od24'])  # 添加当前时刻风力方向
                temp.append(i['od25'])  # 添加当前时刻风级
                temp.append(i['od26'])  # 添加当前时刻降水量
                temp.append(i['od27'])  # 添加当前时刻相对湿度
                temp.append(i['od28'])  # 添加当前时刻空气质量
                # print(temp)
                final_day.append(temp)
                count = count + 1

        # 处理7天数据
        data_7d = body.find('div', {'id': '7d'})  # 找到div标签且id = 7d
        ul = data_7d.find('ul')  # 找到所有的ul标签
        li = ul.find_all('li')  # 找到所有的li标签
        final = []  # 初始化一个列表保存数据
        i = 0  # 控制爬取的天数
        for day in li:  # 遍历找到的每一个li
            if 7 > i > 0:
                temp = []  # 临时存放数据
                date = day.find('h1').string  # 得到日期
                date = date[0:date.index('日')]  # 取出日期号
                temp.append(date)
                inf = day.find_all('p')  # 找出li下面的p标签,提取第一个p标签的值，即天气
                temp.append(inf[0].string)

                tem_low = inf[1].find('i').string  # 找到最低气温
                temp.append(tem_low[:-1])

                if inf[1].find('span') is None:  # 天气预报可能没有最高气温
                    tem_high = None
                else:
                    tem_high = inf[1].find('span').string  # 找到最高气温
                if tem_high[-1] == '℃':
                    temp.append(tem_high[:-1])
                else:
                    temp.append(tem_high)

                wind = inf[2].find_all('span')  # 找到风向
                for j in wind:
                    temp.append(j['title'])

                wind_scale = inf[2].find('i').string  # 找到风级
                index1 = wind_scale.index('级')
                temp.append(int(wind_scale[index1 - 1:index1]))
                final.append(temp)
            i = i + 1
        return final_day, final
        # print(final)

    def get_content_14d(self, html):
        # 处理得到有用信息保存数据文件
        bs = BeautifulSoup(html, "html.parser")  # 创建BeautifulSoup对象
        body = bs.body
        data = body.find('div', {'id': '15d'})  # 找到div标签且id = 15d
        ul = data.find('ul')  # 找到所有的ul标签
        li = ul.find_all('li')  # 找到所有的li标签
        final = []  # 初始化一个列表保存数据
        i = 0  # 控制爬取的天数
        for day in li:  # 遍历找到的每一个li
            if i < 8:
                temp = []  # 临时存放每天的数据
                date = day.find('span', {'class': 'time'}).string  # 得到日期
                date = date[date.index('（') + 1:-2]  # 取出日期号
                temp.append(date)
                weather = day.find('span', {'class': 'wea'}).string  # 找到天气
                temp.append(weather)
                tem = day.find('span', {'class': 'tem'}).text  # 找到温度
                temp.append(tem[tem.index('/') + 1:-1])  # 找到最低气温
                temp.append(tem[:tem.index('/') - 1])  # 找到最高气温
                wind = day.find('span', {'class': 'wind'}).string  # 找到风向
                if '转' in wind:  # 如果有风向变化
                    temp.append(wind[:wind.index('转')])
                    temp.append(wind[wind.index('转') + 1:])
                else:  # 如果没有风向变化，前后风向一致
                    temp.append(wind)
                    temp.append(wind)
                wind_scale = day.find('span', {'class': 'wind1'}).string  # 找到风级
                index1 = wind_scale.index('级')
                temp.append(int(wind_scale[index1 - 1:index1]))
                final.append(temp)
        return final

    def get_html_mw(self, name, html):
        # 处理得到有用信息保存数据文件
        bs = BeautifulSoup(html, "html.parser")  # 创建BeautifulSoup对象
        body = bs.body
        final = [name]
        data_max_all = body.find_all('div', {'class': 'high'})
        data_max = data_max_all[0].string
        data_max = data_max[data_max.index('℃') - 2:data_max.index('℃')].strip()
        data_min_all = body.find_all('div', {'class': 'low'})
        data_min = data_min_all[0].string
        data_min = data_min[data_min.index('℃') - 2:data_min.index('℃')].strip()
        final.append(data_min)
        final.append(data_max)
        return final

    def write_to_csv(self, file_name, data, day):
        if not os.path.exists('./weather_data'):  # 判断是否存在文件夹
            os.mkdir('./weather_data')  # 添加文件夹
        path = os.path.join('./weather_data', file_name)  # 拼接相对路径
        # 保存为CSV
        with open(path, 'w', errors='ignore', newline='') as f:
            if day == 14:
                header = ['日期', '天气', '最低气温', '最高气温', '风向1', '风向2', '风级']
            else:
                header = ['小时', '温度', '风力方向', '风级', '降水量', '相对湿度', '空气质量']
            f_csv = csv.writer(f)
            f_csv.writerow(header)
            f_csv.writerows(data)

    def run(self):
        # 入口函数
        print("Weather test")
        for key, value in self.weather_id_14.items():
            url_id = str(value) + '.shtml'
            url1 = self.url1.format(url_id)
            url2 = self.url2.format(url_id)
            html1 = self.get_html(url1)
            data1, data1_7 = self.get_content_7d(html1)  # 获得1-7天和当天的数据
            html2 = self.get_html(url2)
            data8_14 = self.get_content_14d(html2)  # 获得8-14天数据
            date14 = data1_7 + data8_14
            name1 = key + '1.csv'
            name2 = key + '14.csv'
            self.write_to_csv(name1, data1, 1)  # 保存为CSV
            self.write_to_csv(name2, date14, 14)
            # 每爬取一个页面随机休眠1-2秒钟的时间
            time.sleep(random.randint(1, 2))

        with open('./weather_data\\mw.csv', 'w', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            header = ['城市', '最低温', '最高温']
            f_csv.writerow(header)
            for key, value in self.weather_id_mw.items():
                url_id = str(value) + '.html'
                url3 = self.url3.format(url_id)
                html3 = self.get_html(url3)
                f_csv.writerow(self.get_html_mw(key, html3))
                # 每爬取一个页面随机休眠1-2秒钟的时间
                time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    start = time.time()
    spider = WeatherSpider()  # 实例化一个对象spider
    spider.run()  # 调用入口函数
    clean.run()
    end = time.time()
    # 查看程序执行时间
    print('执行时间:%.2f' % (end - start))  # 爬虫执行时间
