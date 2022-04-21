import os
import math
import json
import jieba
import random
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
            try:
                if c != 0:
                    s += float(c)
                    n += 1
            except:
                a = 1
        if n != 0:
            return round(s / n, 2)
        return 0
    return 0


def sums(L):
    if len(L):
        s = 0
        for c in L:
            s += float(c)
        return round(s, 2)
    return 0


def maxs(L):
    maxl = 0
    for c in L:
        if maxl < c:
            maxl = c
    return maxl


def mins(L):
    minl = 1e9
    for c in L:
        if minl > c:
            minl = c
    return minl


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/<y>/<m>/<d>/<h>/<p>/d101')
def d101(y, m, d, h, p):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时'] == int(h)]
    data = data[data['站点'] == p]
    headers = ['SO2', 'NO2', 'CO', 'O3', 'PM10', 'PM2.5']
    L = []
    for header in headers:
        if header != 'NO2':
            L.append(min(avr(list(data[header])), 200) / 200)
        else:
            L.append(min(avr(list(data[header])), 10) / 10)
    s = {
        "value": round(avr(L), 2)
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<p>/d102')
def d102(y, m, d, p):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['站点'] == p]
    headers = ['SO2', 'NO2', 'CO', 'O3', 'PM10', 'PM2.5']
    maxL = []
    s = []
    for header in headers:
        maxL.append(maxs(list(data[header])))
    for j in range(len(headers)):
        for i in range(24):
            _data = data[data['时'] == int(i)]
            s.append({
                "name": str(i) + "时",
                "type": headers[j],
                "value": avr(list(_data[headers[j]])) / maxL[j]
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<p>/<airType>/d103')
def d103(y, m, p, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['站点'] == p]
    s = []
    for i in range(1, 32):
        for j in range(24):
            _data = data[data['日'] == int(i)]
            _data = _data[_data['时'] == int(j)]
            s.append({
                "x": str(i) + "日",
                "y": avr(list(_data[airType]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<airType>/d104')
def d104(y, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    s = []
    for i in list(data['月'].unique()):
        for j in list(data['站点'].unique()):
            _data = data[data['月'] == int(i)]
            _data = _data[_data['站点'] == j]
            s.append({
                "月": str(i) + "月",
                "站点": str(j),
                "value": avr(list(_data[airType]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<h>/<p>/d10567')
def d10567(y, m, d, h, p):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时'] == int(h)]
    data = data[data['站点'] == p]
    headers = ['SO2', 'NO2', 'CO', 'O3', 'PM10', 'PM2.5']
    s = []
    for header in headers:
        s.append({
            "name": header,
            "value": avr(list(data[header]))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<k>/d108')
def d108(y, m, d, k):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['卡口名称(脱敏)'] == k]
    s = []
    for i in list(data['车辆类型'].unique()):
        _data = data[data['车辆类型'] == i]
        s.append({
            "name": i,
            "value": [
                mins(list(_data['过车数量'])),
                maxs(list(_data['过车数量'])),
            ]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<k>/<carType>/d109abc')
def d109abc(y, m, d, k, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['卡口名称(脱敏)'] == k]
    data = data[data['车辆类型'] == carType]
    maxL = maxs(list(data['过车数量']))
    data = data[data['日'] == int(d)]

    return jsonify(json.loads(_json({
        "value": avr(list(data['过车数量'])) / max(maxL, 100)
    })))


@app.route('/<y>/<types>/d113')
def d113(y, types):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(y)]
    maxL = maxs(list(data[types]))
    s = []
    for i in range(1, 13):
        _data = data[data['月'] == int(i)]
        for j in list(_data['日'].unique()):
            __data = _data[_data['日'] == int(j)]
            s.append({
                "月": str(i) + "月",
                "日": str(j) + "日",
                "value": avr(list(__data[types]))
            })
    return jsonify(json.loads(_json({
        "data": s,
        "max": maxL
    })))


@app.route('/<y>/<types>/d1145')
def d1145(y, types):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(y)]
    data = data.dropna(axis=0, how='any')
    s = []
    for i in range(1, 13):
        _data = data[data['月'] == int(i)]
        s.append({
            "name": str(i) + "月",
            "value": sums(list(_data[types]))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<p>/<airType>/d201')
def d201(y, p, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['站点'] == p]
    if airType == 'CO':
        maxL = 1.5
    else:
        maxL = 100
    s = []
    for i in range(1, 13):
        _data = data[data['月'] == int(i)]
        for j in list(_data['日'].unique()):
            __data = _data[_data['日'] == int(j)]
            s.append({
                "月": str(i) + "月",
                "日": str(j) + "日",
                "value": avr(list(__data[airType]))
            })
    return jsonify(json.loads(_json({
        'data': s,
        'max': maxL
    })))


@app.route('/<y>/<k>/<carType>/d202')
def d202(y, k, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['卡口名称(脱敏)'] == k]
    data = data[data['车辆类型'] == carType]
    s = []
    maxL = maxs(list(data['过车数量']))
    for i in range(1, 13):
        _data = data[data['月'] == int(i)]
        for j in list(_data['日'].unique()):
            __data = _data[_data['日'] == int(j)]
            s.append({
                "月": str(i) + "月",
                "日": str(j) + "日",
                "value": avr(list(__data['过车数量']))
            })
    return jsonify(json.loads(_json({
        "max": maxL,
        "data": s
    })))


@app.route('/<y>/<m>/<d>/<airType>/d203')
def d203(y, m, d, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    s = []
    for j in list(data['站点'].unique()):
        _data = data[data['站点'] == j]
        for i in range(24):
            __data = _data[_data['时'] == int(i)]
            if airType != 'CO':
                s.append({
                    "name": str(i) + "时",
                    "type": j,
                    "value": avr(list(__data[airType])) / 200
                })
            else:
                s.append({
                    "name": str(i) + "时",
                    "type": j,
                    "value": avr(list(__data[airType])) / 10
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<k>/d204')
def d204(y, m, k):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['卡口名称(脱敏)'] == k]
    s = []
    for k in range(1, 32):
        for j in list(data['车辆类型'].unique()):
            _data = data[data['车辆类型'] == j]
            for i in ['2:00-4:00', '7:00-9:00', '10:00-12:00', '17:00-19:00']:
                __data = _data[_data['时段'] == i]
                __data = __data[__data['日'] == int(k)]
                s.append({
                    "name": str(k) + "日" + str(i),
                    "type": j,
                    "value": avr(list(__data['过车数量']))
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<p>/<airType>/d301_2')
def d301_2(y, m, p, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['站点'] == p]
    s = []
    for i in list(data['日'].unique()):
        for j in range(24):
            _data = data[data['日'] == int(i)]
            _data = _data[_data['时'] == int(j)]
            s.append({
                "日": str(i) + "日",
                "时": str(j) + "时",
                "value": avr(list(_data[airType]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<p>/d303_4')
def d303_4(y, p):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['站点'] == p]
    s = []
    headers = ['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']
    for i in range(1, 13):
        _data = data[data['月'] == int(i)]
        for header in headers:
            s.append({
                "name": str(i) + "月",
                "type": header,
                "value": avr(list(_data[header]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<k>/<carType>/d401_2')
def d401_2(y, m, k, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['卡口名称(脱敏)'] == k]
    data = data[data['车辆类型'] == carType]
    maxL = maxs(list(data['过车数量']))
    s = []
    for i in range(1, 32):
        for j in ["2:00-4:00", "7:00-9:00", "10:00-12:00", "17:00-19:00"]:
            _data = data[data['日'] == int(i)]
            _data = _data[_data['时段'] == j]
            s.append({
                "日": str(i) + "日",
                "时段": str(j),
                "value": sums(list(_data['过车数量']))
            })
    return jsonify(json.loads(_json({
        "data": s,
        "max": maxL
    })))


@app.route('/<y>/<k>/d403_4')
def d403_4(y, k):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['卡口名称(脱敏)'] == k]
    s = []
    for i in range(1, 13):
        _data = data[data['月'] == int(i)]
        for j in list(_data['车辆类型'].unique()):
            __data = _data[_data['车辆类型'] == j]
            s.append({
                "name": str(i) + "月",
                "type": j,
                "value": sums(list(__data['过车数量']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<s>/<k>/d501')
def d501(y, m, d, s, k):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时段'] == s]
    data1 = data[data['卡口名称(脱敏)'] == k]
    nodes = []
    links = []
    categories = []
    for i in list(data['名称前缀'].unique()):
        categories.append(i)
    a = 0
    nodes.append({
        "id": "0",
        "name": k.replace(",", "").replace("，", "").replace("'", ""),
        "symbolSize": 50,
        "x": random.random() * 3000 - 1500,
        "y": random.random() * 2000 - 1000,
        "value": len(list(data['卡口名称(脱敏)'].unique())),
        "category": categories.index(
            list(data1['名称前缀'])[0]
        )
    })
    for i in list(data['卡口名称(脱敏)'].unique()):
        a += 1
        _data = data[data['卡口名称(脱敏)'] == i]
        L = []
        for j in list(data['车辆类型'].unique()):
            _data1 = _data[_data['车辆类型'] == j]
            L.append(
                1 -
                abs(avr(list(data1['过车数量'])) - avr(list(_data1['过车数量']))) / max(max(avr(list(data1['过车数量'])), 100), avr(list(_data1['过车数量'])))
            )
        nodes.append({
            "id": str(a),
            "name": i.replace(",", "").replace("，", "").replace("'", ""),
            "symbolSize": avr(L) * 50,
            "x": random.random() * 3000 - 1500,
            "y": random.random() * 2000 - 1000,
            "value": avr(L),
            "category": categories.index(
                list(_data['名称前缀'])[0]
            )
        })
        links.append({
            "source": "0",
            "target": str(a),
        })
    s = {
        "nodes": nodes,
        "links": links,
        "categories": categories
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<s>/<k>/<carType>/d502')
def d502(y, m, d, s, k, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时段'] == s]
    data = data[data['卡口名称(脱敏)'] == k]
    data = data[data['车辆类型'] == carType]
    return jsonify(json.loads(_json({
        "value": avr(list(data['过车数量']))
    })))


@app.route('/<y>/<m>/<k>/d503')
def d503(y, m, k):
    data = pd.read_csv('data/卡口数据.csv')
    types = list(data['车辆类型'].unique())
    maxL = 0
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['卡口名称(脱敏)'] == k]
    s = []
    for i in types:
        s.append({
            "name": i,
            "type": k,
            "value": avr(list(data[data['车辆类型'] == i]['过车数量']))
        })
        maxL = max(maxL, avr(list(data[data['车辆类型'] == i]['过车数量'])))
    return jsonify(json.loads(_json({
        "data": s,
        "max": maxL
    })))


@app.route('/<y>/<m>/<d>/<h>/<airType>/l1')
def l1(y, m, d, h, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时'] == int(h)]
    s = []
    for i in list(data['站点'].unique()):
        _data = data[data['站点'] == i]
        s.append({
            "jd": avr(list(_data['经度'])),
            "wd": avr(list(_data['纬度'])),
            "name": i,
            "value": avr(list(_data[airType])),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<s>/l2')
def l2(y, m, d, s):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时段'] == s]
    s = []
    for i in list(data['卡口名称(脱敏)'].unique()):
        _data = data[data['卡口名称(脱敏)'] == i]
        s.append({
            "jd": avr(list(_data['jd'])),
            "wd": avr(list(_data['wd'])),
            "value": sums(list(_data['过车数量'])),
            "name": i,
            "words": list(_data.sort_values(by=['过车数量'], ascending=False)['车辆类型'])[0]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/<s>/<carType>/l4')
def l4(y, m, d, s, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['日'] == int(d)]
    data = data[data['时段'] == s]
    data = data[data['车辆类型'] == carType]
    s = []
    for i in list(data['卡口名称(脱敏)'].unique()):
        _data = data[data['卡口名称(脱敏)'] == i]
        s.append({
            "jd": avr(list(_data['jd'])),
            "wd": avr(list(_data['wd'])),
            "value": sums(list(_data['过车数量'])),
        })
    return jsonify(json.loads(_json(s)))


app.run(host='127.0.0.1', port=4999, debug=True)
