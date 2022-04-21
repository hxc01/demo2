import json, jieba, os
import random

import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


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


def saveTxt(url, s, encoding="gbk"):
    file = open(url, 'w', encoding=encoding)
    file.write(s)
    file.close()


def _json(s):
    return jsonify(json.loads(str(s).replace("'", '"')))


def counts(L):
    return len(L)


def avr(L):
    if len(L):
        s = 0
        n = 0
        for c in L:
            if c != 0:
                s += c
                n += 1
        if n != 0:
            return s / n
        return 0
    return 0


def sums(L):
    if len(L):
        s = 0
        for c in L:
            s += c
        return s
    return 0

def maxs(L):
    if len(L):
        maxl = -100000
        for c in L:
            maxl = max(maxl, c)
        return maxl
    return -1


@app.route('/<x>div1')
def div1(x):
    data = pd.read_csv('data/' + str(x) + "div1.csv")
    data = data.sort_values(by=['value'], ascending=False)
    name = list(data['name'])
    value = list(data['value'])
    s = []
    for i in range(len(name)):
        s.append({
            "name": name[i],
            "value": value[i]
        })
    return _json(s)


@app.route('/<x><y>div2')
def div2(x, y):
    data = pd.read_csv("data/" + str(x) + str(y) + "div2.csv")
    name1 = list(data['name1'])
    name2 = list(data['name2'])
    value = list(data['value'])
    s = []
    for i in range(len(name1)):
        s.append({
            "name1": name1[i],
            "name2": name2[i],
            "value": value[i]
        })
    return _json(s)


@app.route('/<x>div3')
def div3(x):
    data = pd.read_csv("data/岗位类型" + str(x) + "div3.csv")
    name1 = list(data['name1'])
    name2 = list(data['name2'])
    value = list(data['value'])
    s = []
    for i in range(len(name1)):
        s.append({
            "name": name1[i],
            "type": name2[i],
            "value": value[i],
        })
    return _json(s)


@app.route('/<x>/<y>/<a>/<b>/div4')
def div4(x, y, a, b):
    data = pd.read_csv('data.csv')
    data = data[data['岗位类型'] == x]
    data = data[data['工作类型'] == y]
    data = data[data['工作经验'] == a]
    data = data[data['学历'] == b]
    data = data.sort_values(by=['平均薪资'], ascending=False)
    data.loc[:, "公司名称"] = data['公司名称'].str.replace("'", "")
    Id = list(data['Id'])[:30]
    岗位名称 = list(data['岗位名称'])[:30]
    公司名称 = list(data['公司名称'])[:30]
    平均薪资 = list(data['平均薪资'])[:30]
    学历等级 = list(data['学历等级'])[:30]
    工作类型等级 = list(data['工作类型等级'])[:30]
    工作经验等级 = list(data['工作经验等级'])[:30]
    招聘人数 = list(data['招聘人数'])[:30]
    技能需求 = list(data['技能需求'])[:30]
    岗位描述 = list(data['岗位描述'])[:30]
    s = []
    for i in range(len(岗位名称)):
        s.append({
            "Id": Id[i],
            "岗位名称": 岗位名称[i],
            "公司名称": 公司名称[i],
            "平均薪资": 平均薪资[i],
            "学历等级": 学历等级[i],
            "工作类型等级": 工作类型等级[i],
            "工作经验等级": 工作经验等级[i],
            "招聘人数": 招聘人数[i],
            "技能需求": 技能需求[i],
            "岗位描述": 岗位描述[i]
        })
    return _json(s)


@app.route('/<x><y>div5')
def div5(x, y):
    data = pd.read_csv("data/" + str(x) + str(y) + "div5.csv")
    name = list(data['name'])
    value = list(data['value'])
    s = []
    for i in range(len(name)):
        s.append({
            "name": name[i],
            "value": value[i]
        })
    return _json(s)


@app.route('/<x>/<y>/<a>/<b>/div6')
def div6(x, y, a, b):
    data = pd.read_csv('data.csv')
    data = data[data['岗位类型'] == x]
    data = data[data['工作类型'] == y]
    data = data[data['工作经验'] == a]
    data = data[data['学历'] == b]
    data = data.sort_values(by=['平均薪资'], ascending=False)
    data.loc[:, "公司名称"] = data['公司名称'].str.replace("'", "")
    Id = list(data['Id'])[:30]
    岗位名称 = list(data['岗位名称'])[:30]
    公司名称 = list(data['公司名称'])[:30]
    平均薪资 = list(data['平均薪资'])[:30]
    学历等级 = list(data['学历等级'])[:30]
    工作类型等级 = list(data['工作类型等级'])[:30]
    工作经验等级 = list(data['工作经验等级'])[:30]
    招聘人数 = list(data['招聘人数'])[:30]
    技能需求 = list(data['技能需求'])[:30]
    岗位描述 = list(data['岗位描述'])[:30]
    s = []
    for i in range(len(岗位名称)):
        _s = {}
        _s.update({
            Id[i]: {
                "岗位名称": 岗位名称[i],
                "公司名称": 公司名称[i],
                "平均薪资": 平均薪资[i],
                "学历等级": 学历等级[i],
                "工作类型等级": 工作类型等级[i],
                "工作经验等级": 工作经验等级[i],
                "招聘人数": 招聘人数[i],
                "技能需求": 技能需求[i],
                "岗位描述": 岗位描述[i]
            }
        })
        s.append(_s)
    return _json(s)


@app.route('/<x>m1')
def m1(x):
    data = pd.read_csv("data/" + str(x) + "m1.csv")
    lng = list(data['lng'])
    lat = list(data['lat'])
    value = list(data['value'])
    s = []
    for i in range(len(lat)):
        s.append({"type": "Feature",
                  "properties": {"id": "ak16994521", "mag": value[i], "time": 1507425650893, "felt": 'null',
                                 "tsunami": 0},
                  "geometry": {"type": "Point", "coordinates": [lng[i], lat[i], 0.0]}})
    s = {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "features": s}
    return _json(s)


@app.route('/m2')
def m2():
    data = pd.read_csv("GDP.csv")
    lng = list(data['lng'])
    lat = list(data['lat'])
    value = list(data['value'])
    name = list(data['name'])
    s = []
    for i in range(len(lat)):
        s.append({"type": "Feature",
                  "properties": {"id": name[i], "mag": value[i], "time": 1507425650893, "felt": 'null',
                                 "tsunami": 0},
                  "geometry": {"type": "Point", "coordinates": [lng[i], lat[i], 0.0]}})
    s = {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "features": s}
    return _json(s)


@app.route('/<x>m3')
def m3(x):
    data = pd.read_csv("data/" + str(x) + "m3.csv")
    lng = list(data['lng'])
    lat = list(data['lat'])
    value = list(data['value'])
    s = []
    for i in range(len(lat)):
        s = []
        for i in range(len(lat)):
            s.append({"type": "Feature",
                      "properties": {"id": "ak16994521", "mag": value[i], "time": 1507425650893, "felt": 'null',
                                     "tsunami": 0},
                      "geometry": {"type": "Point", "coordinates": [lng[i], lat[i], 0.0]}})
        s = {
            "type": "FeatureCollection",
            "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
            "features": s}
    return _json(s)


@app.route('/<a>/<b>/<c>/d201')
def d201(a, b, c):
    data = pd.read_csv('base/zyGwlxRatio.csv')
    data = data[data['专业类'] == a]
    data = data.sort_values(by=['关联度'], ascending=False)
    maxl = maxs(list(data['关联度']))
    data = data[data['关联度'] == float(maxl)]
    L = list(data['岗位类型'])
    data = pd.read_csv('base/xbGwlxRatio.csv')
    data = data[data['性别'] == b]
    s = []
    for i in L:
        _data = data[data['岗位类型'] == i]
        s.append({
            "岗位类型": i,
            "关联度": avr(list(_data['关联度']))
        })
    data = pd.DataFrame(s)
    maxl = maxs(list(data['关联度']))
    data = data[data['关联度'] == float(maxl)]
    L = list(data['岗位类型'])
    data = pd.read_csv('base/nlGwlxRatio.csv')
    s = []
    for i in L:
        _data = data[data['岗位类型'] == i]
        s.append({
            "岗位类型": i,
            "关联度": pow(avr(list(_data['最佳年龄'])) - int(c), 2)
        })
    data = pd.DataFrame(s).sort_values(by=['关联度'])
    return _json({"name": list(data['岗位类型'])[0]})


@app.route('/<x>/<y>/d203')
def d203(x, y):
    data = pd.read_csv('data.csv')
    data = data[data['岗位类型'] == x]
    data = data[data['学历'] == y]
    s = []
    公司名称 = list(data['公司名称'].unique())
    for i in range(len(公司名称)):
        _data = data[data['公司名称'] == 公司名称[i]]
        try:
            _s = ""
            for c in list(_data['技能需求']):
                _s += c
            _k = keys(_s)
            _w = weights(_s)
            _s = []
            for c in range(len(_k)):
                _s.append({
                    "name": _k[c],
                    "value": _w[c]
                })
            _s = pd.DataFrame(_s).sort_values(by=['value'], ascending=False)
            _s = list(_s['name'])
            __s = ""
            for c in range(min(len(_s), 5)):
                __s += _s[c] + ","
            s.append({
                "公司名称": 公司名称[i].replace("'", ""),
                "value": min(counts(list(_data['公司名称'])), 50),
                "jd": avr(list(_data['经度'])) + (random.random() * 0.2 - 0.1) * random.random() * random.random(),
                "wd": avr(list(_data['纬度'])) + (random.random() * 0.2 - 0.1) * random.random() * random.random(),
                "技能高频词": __s
            })
        except:
            s.append({
                "公司名称": 公司名称[i].replace("'", ""),
                "value": min(counts(list(_data['公司名称'])), 50),
                "jd": avr(list(_data['经度'])) + (random.random() * 0.2 - 0.1) * random.random() * random.random(),
                "wd": avr(list(_data['纬度'])) + (random.random() * 0.2 - 0.1) * random.random() * random.random(),
                "技能高频词": "无"
            })
    return _json(s)


@app.route('/<x>/<y>/d204')
def d204(x, y):
    data = pd.read_csv('data.csv', usecols=['岗位类型', '岗位名称', '公司名称', '城市', '学历', '工作类型', '工作经验'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == x]
    data = data[data['学历'] == y]
    s = []
    for i in list(data['城市'].unique()):
        _data = data[data['城市'] == i]
        for j in list(data['工作类型'].unique()):
            __data = _data[_data['工作类型'] == j]
            s.append({
                "source": i,
                "target": j,
                "value": counts(list(__data['工作经验']))
            })
            for k in list(data['工作经验'].unique()):
                ___data = __data[__data['工作经验'] == k]
                s.append({
                    "source": j,
                    "target": k,
                    "value": counts(list(___data['工作经验']))
                })
    return _json(s)


@app.route('/<x>/d205')
def d205(x):
    data = pd.read_csv('data.csv')
    data = data[data['公司名称'] == x]
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(len(list(data[headers[0]]))):
        _s = {}
        for j in range(len(L)):
            try:
                if L[j] == '公司名称':
                    _s.update({
                        headers[j]: L[j][i].replace("'", "")
                    })
                else:
                    _s.update({
                        headers[j]: L[j][i]
                    })
            except:
                a = 1
        s.append(_s)
    columns = []
    notColumns = ['Id', '岗位描述', '技能需求', '平均薪资']
    for header in headers:
        if not ('等级' in header) and not ('度' in header) and not (header in notColumns):
            columns.append({
                "prop": header,
                "label": header,
                "width": "250"
            })
    s = {
        "data": s,
        "columns": columns
    }
    return _json(s)


@app.route('/<x>/d206')
def d206(x):
    data = pd.read_csv('data.csv')
    data = data[data['Id'] == int(x)]
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(len(list(data[headers[0]]))):
        _s = {}
        for j in range(len(L)):
            try:
                _s.update({
                    headers[j]: L[j][i]
                })
            except:
                a = 1
        s.append(_s)
    return _json(s)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3050, debug=True)
