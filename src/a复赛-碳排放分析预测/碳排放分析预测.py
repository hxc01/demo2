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


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/<x>/d101')
def d101(x):
    data = pd.read_csv('data/电力数据.csv')
    data = data[data['年份'] == int(x)]
    L2 = list(data['用电类别'].unique())
    s = []
    # for i in L1:
    for j in L2:
        # _data = data[data['年份'] == int(i)]
        _data = data[data['用电类别'] == j]
        s.append({
            # "name": i,
            "name": j,
            "value": avr(list(_data['用电量（千瓦时）']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/d102')
def d102():
    data = pd.read_csv('data/能源数据.csv')
    s = []
    for i in list(data['年份'].unique()):
        for j in list(data['能源类别'].unique()):
            _data = data[data['年份'] == int(i)]
            _data = _data[_data['能源类别'] == j]
            s.append({
                "name": i,
                "type": j,
                "value": avr(list(_data['能耗消耗']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d103')
def d103(x):
    data = pd.read_csv('data/电力数据.csv')
    data = data[data['用电类别'] == x]
    s = []
    for i in list(data['年份'].unique()):
        _data = data[data['年份'] == int(i)]
        s.append({
            "年份": i,
            "用电量": avr(list(_data['用电量（千瓦时）']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/d104')
def d104():
    data = pd.read_csv('data/人口数据.csv')
    s = []
    for i in list(data['年份'].unique()):
        for j in list(data['城镇类别'].unique()):
            _data = data[data['年份'] == int(i)]
            _data = _data[_data['城镇类别'] == j]
            s.append({
                "name": i,
                'type': j,
                "value": avr(list(_data['人口（万人）']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d105')
def d105(x):
    data = pd.read_csv('data/行业经济数据.csv')
    s = []
    data = data[data['年份'] == int(x)]
    for i in list(data['产业'].unique()):
        _data = data[data['产业'] == i]
        _s = []
        for j in list(_data['行业'].unique()):
            __data = _data[_data['行业'] == j]
            _s.append({
                "name": j,
                "value": avr(list(__data['经济增加值（亿元）']))
            })
        s.append({
            "name": i,
            "value": avr(list(_data['经济增加值（亿元）'])),
            "children": _s
        })
    s = {
        "name": str(x) + "年",
        "value": avr(list(data['经济增加值（亿元）'])),
        "children": s
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/d106')
def d106(y):
    data = pd.read_csv('data/空气质量数据.csv')
    data = data[data['城市'] == y]
    s = []
    for i in list(data['年'].unique()):
        _data = data[data['年'] == int(i)]
        for j in range(1, 13):
            __data = _data[_data['月'] == int(j)]
            s.append({
                "年": str(i) + "年",
                "月": str(j) + "月",
                "AQI": avr(list(__data['AQI']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/<airType>/d107')
def d107(x, y, airType):
    data = pd.read_csv('data/空气质量数据.csv')
    data = data[data['年'] == int(x)]
    data = data[data['月'] == int(y)]
    s = []
    for i in list(data['城市'].unique()):
        _data = data[data['城市'] == i]
        s.append({
            "name": i,
            "value": avr(list(_data[airType]))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<airType>/d108')
def d108(x, airType):
    data = pd.read_csv('data/空气质量数据.csv')
    data = data[data['年'] == int(x)]
    s = []
    for i in range(1, 13):
        for j in list(data['城市'].unique()):
            _data = data[data['月'] == int(i)]
            _data = _data[_data['城市'] == j]
            s.append({
                "城市": j,
                "月": str(i) + "月",
                "value": avr(list(_data[airType]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/d109')
def d109():
    data = pd.read_csv('data/地区经济数据.csv')
    L1 = list(data['年份'])
    L2 = list(data['GDP（亿元）'])
    s = []
    for i in range(len(L1)):
        s.append({
            "name": str(L1[i]) + "年",
            "GDP": L2[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<city>/d190')
def d190(y, m, city):
    data = pd.read_csv('data/空气质量数据.csv')
    data = data[data['年'] == int(y)]
    data = data[data['月'] == int(m)]
    data = data[data['城市'] == city]
    s = []
    L = []
    headers = ["SO2", "NO2", "CO", "O3", "PM2.5", "PM10"]
    for header in headers:
        L.append(list(data[header]))
    for i in range(len(L[0])):
        for j in range(len(headers)):
            s.append({
                "name": headers[j],
                "value": L[j][i]
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/<airType>/l1')
def l1(x, y, airType):
    data = pd.read_csv('data/空气质量数据.csv')
    data = data[data['年'] == int(x)]
    data = data[data['月'] == int(y)]
    s = []
    for i in list(data['城市'].unique()):
        _data = data[data['城市'] == i]
        s.append({
            "城市": i,
            "jd": avr(list(_data['经度'])),
            "wd": avr(list(_data['纬度'])),
            "value": avr(list(_data[airType]))
        })
    return jsonify(json.loads(_json(s)))


app.run(host='127.0.0.1', port=5000, debug=True)
