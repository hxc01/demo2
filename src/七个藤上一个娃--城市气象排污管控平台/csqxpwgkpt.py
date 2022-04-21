import math
import os
import jieba
import random
import json

import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS


def keys(article, length=100):
    """
    :param article: 需要切分的文本
    :param length: 关键词数量
    :return:
    """
    global articlelist
    dele = {'。', '！', '？', '的', '“', '”', '（', '）', ' ', '》', '《', '，'}
    words = list(jieba.cut(article))
    # 词频字典
    articleDict = {}
    # 关键词
    articleSet = set(words) - dele
    for w in articleSet:
        if len(w) > 1:
            articleDict[w] = words.count(w)
    return list(sorted(articleDict.keys(), reverse=True))[: length]


def weights(article, length=100):
    """
    :param article: 需要切分的文本
    :param length: 关键词数量
    :return:
    """
    global articlelist
    dele = {'。', '！', '？', '的', '“', '”', '（', '）', ' ', '》', '《', '，'}
    words = list(jieba.cut(article))
    # 词频字典
    articleDict = {}
    # 关键词
    articleSet = set(words) - dele
    for w in articleSet:
        if len(w) > 1:
            articleDict[w] = words.count(w)
    return list(sorted(articleDict.values(), reverse=True))[: length]


def mkdir(path):
    """
    :param path: 创建文件夹位置
    :return:
    """
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        return False
    return True


def saveTxt(url, s, encoding="gbk"):
    file = open(url, 'w', encoding=encoding)
    file.write(s)
    file.close()


def _json(s):
    return str(s).replace("'", '"')


def counts(L):
    return len(L)


def avr(L):
    if len(L):
        s = 0
        n = 0
        for c in L:
            if c != 0:
                s += float(c)
                n += 1
        if n != 0:
            return round(s / n, 2)
        return 0
    return 0


def sums(L):
    if len(L):
        s = 0
        for c in L:
            s += float(c)
        return s
    return 0


def maxs(L):
    maxl = 0
    for c in L:
        if maxl < c:
            maxl = c
    return maxl


def mins(L):
    maxl = 1e8
    for c in L:
        if maxl > c:
            maxl = c
    return maxl


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/<y>/d102')
def d102(y):
    data = pd.read_csv('data/newAQI.csv', usecols=['年', '月', '日', '时', '降水量'])
    data = data[data['年'] == int(y)]
    data = data.dropna(axis=0, how='any')
    s = []
    for i in list(data['月'].unique()):
        _s = []
        _data = data[data['月'] == int(i)]
        for j in list(_data['日'].unique()):
            __data = _data[_data['日'] == int(j)]
            __s = []
            for k in list(__data['时'].unique()):
                ___data = __data[__data['时'] == int(k)]
                __s.append({
                    "name": str(k) + "时",
                    "value": avr(list(___data['降水量']))
                })
            _s.append({
                "name": str(j) + "日",
                "value": avr(list(__data['降水量'])),
                "children": __s
            })
        s.append({
            "name": str(i) + "月",
            "value": avr(list(_data['降水量'])),
            "children": _s
        })
    s = {
        "name": str(y) + "年",
        "value": avr(list(data['降水量'])),
        "children": s
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<h>/<p1>/<p2>/d103')
def d103(y, m, d, h, p1, p2):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时'] == int(h)]
    data1 = data[data['站点'] == p1]
    data2 = data[data['站点'] == p2]
    s = []
    headers = ['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']
    for header in headers:
        s.append({
            "name": p1,
            "value": avr(list(data1[header])),
            "type": header
        })
        s.append({
            "name": p2,
            "value": avr(list(data2[header])),
            "type": header
        })
    maxl = maxs(list(pd.DataFrame(s)['value']))
    return jsonify(json.loads(_json({
        "data": s,
        "max": maxl
    })))


@app.route('/<y>/<d104Type>/d104')
def d104(y, d104Type):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(y)]
    maxl = maxs(list(data[d104Type]))
    s = []
    for i in list(data['月'].unique()):
        for j in list(data['日'].unique()):
            _data = data[data['月'] == int(i)]
            _data = _data[_data['日'] == int(j)]
            s.append({
                "月": str(i) + "月",
                "日": str(j) + "日",
                "value": avr(list(_data[d104Type]))
            })
    return jsonify(json.loads(_json({
        "data": s,
        "max": maxl
    })))


@app.route('/<y>/<m>/<d104Type>/d1041')
def d1041(y, m, d104Type):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    maxl = maxs(list(data[d104Type]))
    s = []
    for i in list(data['日'].unique()):
        for j in list(data['时'].unique()):
            _data = data[data['日'] == int(i)]
            _data = _data[_data['时'] == int(j)]
            s.append({
                "日": str(i) + "日",
                "时": str(j) + "时",
                "value": avr(list(_data[d104Type]))
            })
    return jsonify(json.loads(_json({
        "data": s,
        "max": maxl
    })))


@app.route('/<y>/<m>/<p1>/<airType>/d1051')
def d1051(y, m, p1, airType):
    data1 = pd.read_csv('data/newAQI.csv')
    data1 = data1[data1['年'] == int(y)]
    data1 = data1[data1['月'] == int(m)]
    data2 = pd.read_csv('data/站点监测数据.csv')
    data2 = data2[data2['年'] == int(y)]
    data2 = data2[data2['月'] == int(m)]
    data2 = data2[data2['站点'] == p1]
    s = []
    for i in list(data1['日'].unique()):
        for j in list(data2['时'].unique()):
            _data1 = data1[data1['日'] == int(i)]
            _data1 = _data1[_data1['时'] == int(j)]
            _data2 = data2[data2['日'] == int(i)]
            _data2 = _data2[_data2['时'] == int(j)]
            s.append({
                "日": str(i) + "日",
                "时": str(j) + "时",
                "风速": avr(list(_data1['风速'])),
                "size": avr(list(_data2[airType]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<p1>/<airType>/d105')
def d105(y, p1, airType):
    data1 = pd.read_csv('data/newAQI.csv')
    data1 = data1[data1['年'] == int(y)]
    data2 = pd.read_csv('data/站点监测数据.csv')
    data2 = data2[data2['年'] == int(y)]
    data2 = data2[data2['站点'] == p1]
    s = []
    for i in list(data1['月'].unique()):
        for j in list(data2['日'].unique()):
            _data1 = data1[data1['月'] == int(i)]
            _data1 = _data1[_data1['日'] == int(j)]
            _data2 = data2[data2['月'] == int(i)]
            _data2 = _data2[_data2['日'] == int(j)]
            s.append({
                "月": str(i) + "月",
                "日": str(j) + "日",
                "风速": avr(list(_data1['风速'])),
                "size": avr(list(_data2[airType]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<carType>/d106')
def d106(y, m, d, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['车辆类型'] == carType]
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    length = 30
    _data = data[data['时段'] == '2:00-4:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s1.append({
            "name": i,
            "value": avr(list(__data['过车数量']))
        })

    _data = data[data['时段'] == '7:00-9:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s2.append({
            "name": i,
            "value": avr(list(__data['过车数量']))
        })

    _data = data[data['时段'] == '10:00-12:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s3.append({
            "name": i,
            "value": avr(list(__data['过车数量']))
        })

    _data = data[data['时段'] == '17:00-19:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s4.append({
            "name": i,
            "value": avr(list(__data['过车数量']))
        })

    s = []
    for i in range(length - 1):
        s.append({
            "source": s1[i]['name'], "target": s2[i]['name'], "value": s1[i]['value']
        })
        s.append({
            "source": s2[i]['name'], "target": s3[i]['name'], "value": s2[i]['value']
        })
        s.append({
            "source": s3[i]['name'], "target": s4[i]['name'], "value": s3[i]['value']
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<s>/<kakou>/d107')
def d107(y, m, d, s, kakou):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['卡口名称(脱敏)'] == kakou]
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时段'] == s]
    s = []
    for i in list(data['车辆类型'].unique()):
        _data = data[data['车辆类型'] == i]
        s.append({
            "车辆类型": i,
            "过车数量": avr(list(_data['过车数量']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/d108')
def d108(y, m, d):
    data = pd.read_csv('data/卡口数据.csv', usecols=['年', '月', '日', '卡口名称(脱敏)', '车辆类型', '过车数量'])
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)].sort_values(by=['过车数量'], ascending=False)
    s = []
    for i in list(data['卡口名称(脱敏)'].unique()):
        for j in list(data['车辆类型'].unique()):
            _data = data[data['卡口名称(脱敏)'] == i]
            _data = _data[_data['车辆类型'] == j]
            s.append({
                "卡口名称": i,
                "车辆类型": j,
                "过车数量": avr(list(_data['过车数量']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/d109')
def d109(y, m):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    s = []
    fx = ['N', 'EN', 'E', 'ES', 'S', 'WS', 'W', 'WN']
    for i in list(data['日'].unique()):
        _data = data[data['日'] == int(i)]
        try:
            if str(list(_data['天气现象'])[0]) == '晴':
                if avr(list(_data['降水量'])) == 0:
                    s.append({
                        "date": str(i) + "日",
                        "maxTemp": maxs(list(_data['气温'])),
                        "minTemp": mins(list(_data['气温'])),
                        "rain": 0,
                        "sunny": 1,
                        "windSpeed": avr(list(_data['风速'])),
                        "windDir": fx[int(list(_data['风向'])[0]) // 45]
                    })
                else:
                    s.append({
                        "date": str(i) + "日",
                        "maxTemp": maxs(list(_data['气温'])),
                        "minTemp": mins(list(_data['气温'])),
                        "rain": 1,
                        "sunny": 1,
                        "windSpeed": avr(list(_data['风速'])),
                        "windDir": fx[int(list(_data['风向'])[0]) // 45]
                    })
            else:
                if avr(list(_data['降水量'])) == 0:
                    s.append({
                        "date": str(i) + "日",
                        "maxTemp": maxs(list(_data['气温'])),
                        "minTemp": mins(list(_data['气温'])),
                        "rain": 0,
                        "sunny": 0,
                        "windSpeed": avr(list(_data['风速'])),
                        "windDir": fx[int(list(_data['风向'])[0]) // 45]
                    })
                else:
                    s.append({
                        "date": str(i) + "日",
                        "maxTemp": maxs(list(_data['气温'])),
                        "minTemp": mins(list(_data['气温'])),
                        "rain": 1,
                        "sunny": 0,
                        "windSpeed": avr(list(_data['风速'])),
                        "windDir": fx[int(list(_data['风向'])[0]) // 45]
                    })
        except:
            a = 1
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<s>/<k1>/<k2>/<k3>/<k4>/<carType>/d110')
def d110(y, m, d, s, k1, k2, k3, k4, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['车辆类型'] == carType]
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时段'] == s]
    s = []
    _data = data[data['卡口名称(脱敏)'] == k1]
    s.append({
        "title": k1,
        "ranges": [
            round(maxs(list(data['过车数量'])) * 0.3, 0),
            round(maxs(list(data['过车数量'])) * 0.6, 0),
            round(maxs(list(data['过车数量'])) * 1.2, 0),
        ],
        "measures": [
            round(avr(list(_data['过车数量'])), 0),
        ],
        "target": round(avr(list(_data['过车数量'])) * 0.8, 0),
    })
    _data = data[data['卡口名称(脱敏)'] == k2]
    s.append({
        "title": k2,
        "ranges": [
            round(maxs(list(data['过车数量'])) * 0.3, 0),
            round(maxs(list(data['过车数量'])) * 0.6, 0),
            round(maxs(list(data['过车数量'])) * 1.2, 0),
        ],
        "measures": [
            round(avr(list(_data['过车数量'])), 0),
        ],
        "target": round(avr(list(_data['过车数量'])) * 0.8, 0),
    })
    _data = data[data['卡口名称(脱敏)'] == k3]
    s.append({
        "title": k3,
        "ranges": [
            round(maxs(list(data['过车数量'])) * 0.3, 0),
            round(maxs(list(data['过车数量'])) * 0.6, 0),
            round(maxs(list(data['过车数量'])) * 1.2, 0),
        ],
        "measures": [
            round(avr(list(_data['过车数量'])), 0),
        ],
        "target": round(avr(list(_data['过车数量'])) * 0.8, 0),
    })
    _data = data[data['卡口名称(脱敏)'] == k4]
    s.append({
        "title": k4,
        "ranges": [
            round(maxs(list(data['过车数量'])) * 0.3, 0),
            round(maxs(list(data['过车数量'])) * 0.6, 0),
            round(maxs(list(data['过车数量'])) * 1.2, 0),
        ],
        "measures": [
            round(avr(list(_data['过车数量'])), 0),
        ],
        "target": round(avr(list(_data['过车数量'])) * 0.8, 0),
    })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<k>/d1101')
def d1101(y, m, d, k):
    s1 = "■ "
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['卡口名称(脱敏)'] == k].sort_values(by=['过车数量'], ascending=False)
    s1 += '今日最多的三种车辆类型及其分析：'
    for i in list(data['车辆类型'].unique())[:3]:
        _data = pd.read_csv('data/卡口数据.csv')
        _data = _data[_data['车辆类型'] == i]
        max1 = maxs(list(_data['过车数量']))
        _data = _data[_data['卡口名称(脱敏)'] == k]
        max2 = maxs(list(_data['过车数量']))
        _data = data[data['车辆类型'] == i]
        value = round(avr(list(_data['过车数量'])), 0)
        s1 += i + "过车数量为" + str(value) + "," + "占本站同车型历史最高的" + str(round(value / max2, 2)) + ";"
        s1 += "占全站同车型历史最高的" + str(round(value / max1, 2)) + "。"

    jd = avr(list(data['jd']))
    wd = avr(list(data['wd']))
    s2 = "■ "
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    maxSO2 = min(maxs(list(data['SO2'])), 200)
    maxNO2 = min(maxs(list(data['NO2'])), 200)
    maxCO = min(maxs(list(data['CO'])), 200)
    maxO3 = min(maxs(list(data['O3'])), 200)
    maxPM10 = min(maxs(list(data['PM10'])), 200)
    maxPM25 = min(maxs(list(data['PM2.5'])), 200)
    data = data[data['日'] == int(d)]
    zdDis = []
    s2 += "对于较近的两个检测站点的影响情况为："
    for i in list(data['站点'].unique()):
        _data = data[data['站点'] == i]
        zdDis.append({
            "name": i,
            "value": pow((avr(list(_data['经度'])) - jd), 2) + pow((avr(list(_data['纬度'])) - wd), 2)
        })
    zdDis = pd.DataFrame(zdDis).sort_values(by=['value'])
    for i in list(zdDis['name'])[:2]:
        _data = data[data['站点'] == i]
        s2 += "站点" + i
        s2 += "的SO2峰值占比为" + str(round(avr(list(_data['SO2'])) / maxSO2, 2)) + ";"
        s2 += "NO2峰值占比为" + str(round(avr(list(_data['NO2'])) / maxNO2, 2)) + ";"
        s2 += "CO峰值占比为" + str(round(avr(list(_data['CO'])) / maxCO, 2)) + ";"
        s2 += "O3峰值占比为" + str(round(avr(list(_data['O3'])) / maxO3, 2)) + ";"
        s2 += "PM10峰值占比为" + str(round(avr(list(_data['PM10'])) / maxPM10, 2)) + ";"
        s2 += "PM2.5峰值占比为" + str(round(avr(list(_data['PM2.5'])) / maxPM25, 2)) + "。"
    return jsonify(json.loads(_json({
        "s1": s1,
        "s2": s2
    })))


@app.route('/<y>/<m>/<d>/<h>/<p>/d111_112')
def d111_112(y, m, d, h, p):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时'] == int(h)]
    data = data[data['站点'] == p]
    s = [{
        "站点": p,
        "污染指数": round(
            avr([
                avr(list(data['SO2'])) / 200,
                avr(list(data['NO2'])) / 10,
                avr(list(data['PM2.5'])) / 200,
                avr(list(data['O3'])) / 200,
                avr(list(data['CO'])) / 200,
                avr(list(data['PM10'])) / 200,
            ]), 2
        )
    }]
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<p>/<airType>/d113_114')
def d113_114(y, m, d, p, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['站点'] == p]
    s = []
    for i in range(24):
        _data = data[data['时'] == int(i)]
        s.append({
            "时间": str(i) + "时",
            "value": avr(list(_data[airType]))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<p1>/<p2>/<airType>/d115')
def d115(y, m, d, p1, p2, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data1 = data[data['站点'] == p1]
    data2 = data[data['站点'] == p2]
    s = []
    for i in range(24):
        _data1 = data1[data1['时'] == int(i)]
        s.append({
            "时间": str(i) + "时",
            "站点": p1,
            "value": avr(list(_data1[airType]))
        })
        _data2 = data2[data2['时'] == int(i)]
        s.append({
            "时间": str(i) + "时",
            "站点": p2,
            "value": avr(list(_data2[airType]))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<kakou>/d116')
def d116(y, m, d, kakou):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['卡口名称(脱敏)'] == kakou]
    s = []
    for i in list(data['车辆类型'].unique()):
        _data = data[data['车辆类型'] == i]
        s.append({
            "车辆类型": i,
            "过车数量": sums(list(_data['过车数量']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<sd>/<carType>/l1')
def l1(y, m, d, sd, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['车辆类型'] == carType]
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时段'] == sd].sort_values(by=['过车数量'], ascending=False)
    s = []
    for i in list(data['卡口名称(脱敏)'].unique()):
        for j in list(data['车辆类型'].unique()):
            _data = data[data['卡口名称(脱敏)'] == i]
            _data = _data[_data['车辆类型'] == j]
            s.append({
                "卡口名称": i,
                "jd": avr(list(_data['jd'])),
                "wd": avr(list(_data['wd'])),
                "value": avr(list(_data['过车数量']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<h>/<airType>/l2')
def l2(y, m, d, h, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时'] == int(h)]
    s = []
    for i in list(data['站点'].unique()):
        _data = data[data['站点'] == i]
        s.append({
            "站点": i,
            "jd": avr(list(_data['经度'])),
            "wd": avr(list(_data['纬度'])),
            "value": avr(list(_data[airType]))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<s>/<carType>/l3')
def l3(y, m, d, s, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['车辆类型'] == carType]
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    length = 30
    _data = data[data['时段'] == '2:00-4:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s1.append({
            "name": i,
            "value": avr(list(__data['过车数量'])),
            'jd': avr(list(__data['jd'])),
            'wd': avr(list(__data['wd'])),
        })

    _data = data[data['时段'] == '7:00-9:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s2.append({
            "name": i,
            "value": avr(list(__data['过车数量'])),
            'jd': avr(list(__data['jd'])),
            'wd': avr(list(__data['wd'])),
        })

    _data = data[data['时段'] == '10:00-12:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s3.append({
            "name": i,
            "value": avr(list(__data['过车数量'])),
            'jd': avr(list(__data['jd'])),
            'wd': avr(list(__data['wd'])),
        })

    _data = data[data['时段'] == '17:00-19:00'].sort_values(by=['过车数量'], ascending=False)
    for i in list(_data['卡口名称(脱敏)'])[:length]:
        __data = _data[_data['卡口名称(脱敏)'] == i]
        s4.append({
            "name": i,
            "value": avr(list(__data['过车数量'])),
            'jd': avr(list(__data['jd'])),
            'wd': avr(list(__data['wd'])),
        })

    _s = []
    for i in range(length - 1):
        if s == '2:00-4:00':
            _s.append({
                "卡口名称1": s1[i]['name'],
                "卡口名称2": s2[i]['name'],
                "jd1": s1[i]['jd'],
                "wd1": s1[i]['wd'],
                "jd2": s2[i]['jd'],
                "wd2": s2[i]['wd'],
                "value": s1[i]['value']
            })
        elif _s == '7:00-9:00':
            s.append({
                "卡口名称1": s2[i]['name'],
                "卡口名称2": s3[i]['name'],
                "jd1": s2[i]['jd'],
                "wd1": s2[i]['wd'],
                "jd2": s3[i]['jd'],
                "wd2": s3[i]['wd'],
                "value": s2[i]['value']
            })
        elif _s == '10:00-12:00':
            s.append({
                "卡口名称1": s3[i]['name'],
                "卡口名称2": s4[i]['name'],
                "jd1": s3[i]['jd'],
                "wd1": s3[i]['wd'],
                "jd2": s4[i]['jd'],
                "wd2": s4[i]['wd'],
                "value": s3[i]['value']
            })
        else:
            _s.append({
                "卡口名称1": s4[i]['name'],
                "卡口名称2": s1[i]['name'],
                "jd1": s4[i]['jd'],
                "wd1": s4[i]['wd'],
                "jd2": s1[i]['jd'],
                "wd2": s1[i]['wd'],
                "value": s4[i]['value']
            })
    return jsonify(json.loads(_json(_s)))


@app.route('/<y>/<m>/<d>/<length1>/<length2>/l4')
def l4(y, m, d, length1, length2):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data1 = pd.read_csv('data/站点监测数据.csv')
    data1 = data1[data1['年'] == int(y)]
    data1 = data1[data1['月'] == int(m)]
    data1 = data1[data1['日'] == int(d)]
    s = []
    时 = list(data['时'].unique())
    for i in list(data1['站点'].unique()):
        _data1 = data1[data1['站点'] == i]
        jd1 = avr(list(_data1['经度']))
        wd1 = avr(list(_data1['纬度']))
        for j in range(int(length1), int(length2)):
            _data = data[data['时'] == int(时[j])]
            try:
                jd2 = jd1 + math.cos(
                    avr(list(_data['风向']))
                ) * avr(list(_data['风速'])) * 8 / 111
                wd2 = wd1 + math.sin(
                    avr(list(_data['风向']))
                ) * avr(list(_data['风速'])) * 8 / 111
                s.append({
                    "站点": i,
                    "jd1": jd1,
                    "wd1": wd1,
                    "jd2": jd2,
                    "wd2": wd2,
                })
                jd1 = jd2
                wd1 = wd2
            except:
                a = 1
    return jsonify(json.loads(_json(s)))


app.run(host='127.0.0.1', port=2022, debug=True)
