import pandas as pd

path = './weather_data\\{}'
city = ['德州', '济南', '聊城', '菏泽', '济宁', '泰安', '莱芜', '枣庄', '临沂', '日照', '淄博', '滨州',
        '东营', '潍坊', '青岛', '烟台', '威海']


def clean_data(path):
    data = pd.read_csv(path, encoding='gbk', header=0)
    data = data.fillna(axis=0, method='ffill')
    data = data.fillna(axis=0, method='bfill')
    data.to_csv(path, encoding='gbk', index=0)


def run():
    print('开始清洗')
    for index in city:
        path_1d = path.format(index + '1.csv')
        path_14d = path.format(index + '14.csv')
        clean_data(path_1d)
        clean_data(path_14d)


if __name__ == '__main__':
    run()
