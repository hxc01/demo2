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
            return s / n
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


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/<year>/<month>/<day>/div1')
def div1(year, month, day):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    data = data[data['日'] == int(day)]
    s = [{
        "气温": round(avr(list(data['气温'])), 2),
        "风速": round(avr(list(data['风速'])), 2),
        "降水量": round(sums(list(data['降水量'])), 2),
        "天气现象": list(data['天气现象'])[0],
        "日期": list(data['日期'])[0],
        "AQI": list(data['AQI'])[0]
    }]
    return jsonify(json.loads(_json(s)))


@app.route('/<type1>/<airType>/div2')
def div2(type1, airType):
    data = pd.read_csv('data/newAQI.csv')
    data = data.dropna(axis=0, how='any')
    date = list(data['日期'].unique())
    x = []
    y = []
    for i in date:
        _data = data[data['日期'] == i]
        x.append(round(avr(list(_data[type1])), 2))
        y.append(round(avr(list(_data[airType])), 2))
    s = [{
        "data1": x,
        "日期": date,
        "data2": y
    }]
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/div3')
def div3(year, month):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    s = []
    for i in list(data['天气现象'].unique()):
        if i != "0":
            s.append({
                "name": i,
                "value": len(list(data[data['天气现象'] == i]['天气现象']))
            })
        else:
            s.append({
                "name": '',
                "value": len(list(data[data['天气现象'] == i]['天气现象']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/<day>/<shi>/<carType>/div4_1')
def div4_1(year, month, day, shi, carType):
    data = pd.read_csv('data/卡口数据.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    data = data[data['日'] == int(day)]
    data = data[data['时段'] == shi]
    data = data[data['车辆类型'] == carType]
    s = []
    jd = list(data['jd'])
    wd = list(data['wd'])
    value = list(data['过车数量'])
    name = list(data['卡口名称(脱敏)'])

    for i in range(len(jd)):
        s.append({
            "name": name[i],
            "jd": jd[i],
            "wd": wd[i],
            "value": value[i],
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/<day>/<hour>/<airType>/div4_2')
def div4_2(year, month, day, hour, airType):
    data = pd.read_csv('data/站点监测数据.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    data = data[data['日'] == int(day)]
    data = data[data['时'] == int(hour)]
    s = []
    for i in list(data['站点'].unique()):
        _data = data[data['站点'] == i]
        s.append({
            "name": i,
            "jd": list(_data['经度'])[0],
            "wd": list(_data['纬度'])[0],
            "value": avr(list(_data[airType]))
        })
    return jsonify(json.loads(_json(s)))



@app.route('/<type1>/div5')
def div5(type1):
    data = pd.read_csv('data/newAQI.csv')
    data = data.dropna(axis=0, how='any')
    date = list(data['日期'].unique())
    s = []
    for i in date:
        if type1 != '降水量':
            s.append([
                i,
                avr(list(data[data['日期'] == i][type1]))
            ])
        else:
            s.append([
                i,
                sums(list(data[data['日期'] == i][type1]))
            ])
    s = [{
        "data": s,
        "max": maxs(list(data[type1]))
    }]
    return jsonify(json.loads(_json(s)))


@app.route('/<airType>/<year>/div6')
def div6(airType, year):
    data = pd.read_csv('data/newAQI.csv')
    data = data[data['年'] == int(year)]
    data = data.dropna(axis=0, how='any')
    s = []
    for i in list(data['月'].unique()):
        for j in list(data['日'].unique()):
            _data = data[data['月'] == i]
            _data = _data[_data['日'] == j]
            s.append([
                year + "-" + str(i) + "-" + str(j),
                round(avr(list(_data[airType])), 2)
            ])
    s = [{
        "data": s,
        "max": maxs(list(data[airType]))
    }]
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/div7')
def div7(year, month):
    data = pd.read_csv('data/站点监测数据.csv')
    data1 = pd.read_csv('data/newAQI.csv', usecols=['年', '月', '日', 'AQI', '质量等级'])
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    data1 = data1.dropna(axis=0, how='any')
    data1 = data1[data1['年'] == int(year)]
    data1 = data1[data1['月'] == int(month)]
    s = {}
    maxl = 0
    for i in list(data['站点'].unique()):
        _s = []
        for j in list(data['日'].unique()):
            _data = data[data['站点'] == i]
            _data = _data[_data['日'] == int(j)]
            _data1 = data1[data1['日'] == int(j)]
            _s.append([
                int(j),
                list(_data1['AQI'])[0],
                avr(list(_data['PM2.5'])),
                avr(list(_data['PM10'])),
                avr(list(_data['CO'])),
                avr(list(_data['NO2'])),
                avr(list(_data['SO2'])),
                list(_data1['质量等级'])[0]
            ])
            maxl = max(maxs([list(_data1['AQI'])[0]]), maxl)
        s.update({
            i: _s
        })
    s.update({
        "maxs": maxl
    })
    s = [s]
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/<day>/<shiduan>/div8')
def div8(year, month, day, shiduan):
    data = pd.read_csv('data/交警卡口半年全量数据.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    data = data[data['日'] == int(day)]
    data = data[data['时段'] == shiduan]
    max_s = {}
    for i in list(data['车辆类型'].unique()):
        max_s.update({
            i: maxs(list(data[data['车辆类型'] == i]['过车数量']))
        })
    s = []
    for i in list(data['车辆类型'].unique()):
        for j in list(data['卡口名称(脱敏)'].unique()):
            _data = data[data['车辆类型'] == i]
            _data = _data[_data['卡口名称(脱敏)'] == j]
            if sums(list(_data['过车数量'])):
                s.append({
                    "卡口名称": j,
                    "车辆类型": i,
                    "color": sums(list(_data['过车数量'])),
                    "value": round(sums(list(_data['过车数量']))/max_s[i], 2),
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<carType>/<kakou>/div8_1')
def div8_1(year, carType, kakou):
    data = pd.read_csv('data/交警卡口半年全量数据.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['车辆类型'] == carType]
    data = data[data['卡口名称(脱敏)'] == kakou]
    max_s = maxs(list(data['过车数量']))
    s = []
    for i in list(data['月'].unique()):
        for j in list(data['日'].unique()):
            _data = data[data['月'] == int(i)]
            _data = _data[_data['日'] == int(j)]
            s.append({
                "月": str(i),
                "日": str(j),
                "value": round(avr(_data['过车数量']) / max_s, 2)
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/<carType>/<kakou>/div8_2')
def div8_2(year, carType, kakou, month):
    data = pd.read_csv('data/交警卡口半年全量数据.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['车辆类型'] == carType]
    data = data[data['卡口名称(脱敏)'] == kakou]
    data = data[data['月'] == int(month)]
    max_s = maxs(list(data['过车数量']))
    s = []
    for i in list(data['日'].unique()):
        for j in ['17:00-19:00', '10:00-12:00', '7:00-9:00', '2:00-4:00']:
            _data = data[data['日'] == int(i)]
            _data = _data[_data['时段'] == j]
            s.append({
                "日": str(i),
                "时段": str(j),
                "value": round(avr(_data['过车数量']) / max_s, 2)
            })
    return jsonify(json.loads(_json(s)))


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=1112, debug=True)
