import os
import math
import json
import jieba
import random
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS


def keys(article, length=500):
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


def weights(article, length=500):
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


@app.route('/<date>/<ids>/l1')
def l1(date, ids):
    y = int(date.split("-")[0])
    m = int(date.split("-")[1])
    d = int(date.split("-")[2])
    date = str(y) + "-" + ("0" + str(m))[-2:] + "-" + ("0" + str(d))[-2:]
    data = pd.read_csv('data/密接轨迹/' + date + ".csv")
    data = data[data['id'] == int(ids)]
    s = []
    for i in range(23):
        data1 = data[data['h'] == int(i)]
        data2 = data[data['h'] == int(i + 1)]
        s.append({
            "id": avr(list(data1['id'])),
            "city": list(data['city'])[0],
            "jd1": avr(list(data1['jd'])),
            "wd1": avr(list(data1['wd'])),
            "jd2": avr(list(data2['jd'])),
            "wd2": avr(list(data2['wd'])),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/l2')
def l2(date):
    y = int(date.split("-")[0])
    m = int(date.split("-")[1])
    d = int(date.split("-")[2])
    date = str(y) + "-" + ("0" + str(m))[-2:] + "-" + ("0" + str(d))[-2:]
    citys = list(pd.read_csv('data/城市经纬度.csv')['城市'])
    s = []
    for city in citys:
        try:
            if "市" in city:
                data = pd.read_csv('data/疫情数据/' + city + ".csv")
            else:
                data = pd.read_csv('data/疫情数据/' + city + "市.csv")
            jwd = pd.read_csv('data/城市经纬度.csv')
            jwd = jwd[jwd['城市'] == city]
            data.loc[:, "年"] = data['日期'].str.replace("-", "").astype('int64') // 10000
            data.loc[:, "月"] = data['日期'].str.replace("-", "").astype('int64') // 100 % 100
            data.loc[:, "日"] = data['日期'].str.replace("-", "").astype('int64') % 100
            data = data[data['日期'] == date]
            s.append({
                "jd": avr(list(jwd['经度'])),
                "wd": avr(list(jwd['纬度'])),
                "value": sums(list(data['确诊'])) - sums(list(data['治愈'])) - sums(list(data['死亡']))
            })
        except:
            a = 1
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d101')
def d101(date):
    y = int(date.split("-")[0])
    m = int(date.split("-")[1])
    d = int(date.split("-")[2])
    date = str(y) + "-" + ("0" + str(m))[-2:] + "-" + ("0" + str(d))[-2:]
    data = pd.read_csv('data/密接轨迹/' + date + ".csv")
    headers = list(data.head(0))
    L = []
    s = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(len(L[0])):
        _s = {}
        for j in range(len(L)):
            _s.update({
                headers[j]: L[j][i]
            })
        s.append(_s)
    columns = [{
        "prop": "id",
        "label": "id",
        "width": "150"
    }, {
        "prop": "city",
        "label": "到访城市",
        "width": "150"
    }]
    s = {
        "data": s,
        "columns": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<city>/d102')
def d102(city):
    if "市" in city:
        data = pd.read_csv('data/疫情数据/' + city + ".csv")
    else:
        data = pd.read_csv('data/疫情数据/' + city + "市.csv")
    s = []
    for i in list(data['日期'].unique()):
        _data = data[data['日期'] == i]
        s.append({
            "date": i,
            "value": avr(list(_data['累计确诊'])),
            "type": "累计确诊"
        })
        s.append({
            "date": i,
            "value": avr(list(_data['累计疑似'])),
            "type": "累计疑似"
        })
        s.append({
            "date": i,
            "value": avr(list(_data['累计治愈'])),
            "type": "累计治愈"
        })
        s.append({
            "date": i,
            "value": avr(list(_data['累计死亡'])),
            "type": "累计死亡"
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/d103')
def d103(y, m):
    citys = list(pd.read_csv('data/城市经纬度.csv')['城市'])
    s = []
    for city in citys:
        try:
            if "市" in city:
                data = pd.read_csv('data/疫情数据/' + city + ".csv")
            else:
                data = pd.read_csv('data/疫情数据/' + city + "市.csv")
            data.loc[:, "年"] = data['日期'].str.replace("-", "").astype('int64') // 10000
            data.loc[:, "月"] = data['日期'].str.replace("-", "").astype('int64') // 100 % 100
            data.loc[:, "日"] = data['日期'].str.replace("-", "").astype('int64') % 100
            data = data[data['年'] == int(y)]
            data = data[data['月'] == int(m)]
            for i in list(data['日'].unique()):
                _data = data[data['日'] == int(i)]
                s.append({
                    "city": city,
                    "day": str(i) + "日",
                    "value": avr(list(_data['累计确诊'])),
                    "size": avr(list(_data['累计确诊'])) / maxs(list(data['累计确诊']))
                })
        except:
            a = 1
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/d104')
def d104(y):
    citys = list(pd.read_csv('data/城市经纬度.csv')['城市'])
    s = []
    bar = []
    pie = []
    line = []
    for city in citys:
        try:
            if "市" in city:
                data = pd.read_csv('data/疫情数据/' + city + ".csv")
            else:
                data = pd.read_csv('data/疫情数据/' + city + "市.csv")
            data.loc[:, "年"] = data['日期'].str.replace("-", "").astype('int64') // 10000
            data.loc[:, "月"] = data['日期'].str.replace("-", "").astype('int64') // 100 % 100
            data.loc[:, "日"] = data['日期'].str.replace("-", "").astype('int64') % 100
            data = data[data['年'] == int(y)]
            for c in ['确诊', '疑似', '治愈', '死亡']:
                bar.append({
                    "city": city,
                    "type": c,
                    "value": sums(list(data[c]))
                })
            pie.append({
                "city": city,
                "value": sums(list(data['确诊'])) - sums(list(data['治愈'])) - sums(list(data['死亡']))
            })
            for i in list(data['月'].unique()):
                _data = data[data['月'] == int(i)]
                line.append({
                    "date": str(i) + "月",
                    "city": city,
                    "value": sums(list(_data['确诊'])) - sums(list(_data['治愈'])) - sums(list(_data['死亡']))
                })
        except:
            a = 1
    s = {
        "line": line,
        "pie": pie,
        "bar": bar
    }
    return jsonify(json.loads(_json(s)))


@app.route('/d105')
def d105():
    f = open('data/舆论数据/评论数据', 'r')
    citys = pd.read_csv('data/城市经纬度.csv')
    jds = list(citys['经度'])
    wds = list(citys['纬度'])
    citys = list(citys['城市'])
    s = ""
    for c in f:
        s += c
    _k = keys(s)
    _w = weights(s)
    s = []
    date = ['2022-03-26', '2022-03-27', '2022-03-28', '2022-03-29', '2022-03-30', '2022-03-31', '2022-04-01', '2022-04-02']
    for i in range(len(_k)):
        ind = int(random.random() * 100) % 15
        city = citys[ind]
        jd = jds[ind]
        wd = wds[ind]
        _jd = jd + random.random() * 0.5
        _wd = wd + random.random() * 0.5
        dateId = int(random.random() * 100) % 8
        s.append({
            "name": _k[i],
            "value": _w[i] * random.random(),
            "date": date[dateId],
            "jd": _jd,
            "wd": _wd,
            'dateId': dateId,
            "city": city,
        })
    return jsonify(json.loads(_json(s)))


def guiji(date):
    mkdir('data/密接轨迹')
    citys = pd.read_csv('data/城市经纬度.csv')
    jds = list(citys['经度'])
    wds = list(citys['纬度'])
    citys = list(citys['城市'])
    s = []
    for i in range(1, 10):
        ind = int(random.random() * 100) % 15
        city = citys[ind]
        jd = jds[ind]
        wd = wds[ind]
        for j in range(24):
            _jd = jd + random.random() * 0.5
            _wd = wd + random.random() * 0.5
            s.append({
                "id": i,
                "jd": _jd,
                "wd": _wd,
                "h": j,
                "city": city,
            })
    pd.DataFrame(s).to_csv('data/密接轨迹/' + date + ".csv", index=0)


"""for j in range(10, 32):
    guiji("2022-03-" + ("0" + str(j))[-2:])
for j in range(1, 6):
    guiji("2022-04-" + ("0" + str(j))[-2:])"""

app.run(host='127.0.0.1', port=5000, debug=True)
