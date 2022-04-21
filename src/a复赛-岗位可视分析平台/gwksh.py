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


@app.route('/<city>/<gwlx>/<xl>/岗位描述')
def div1ms(city, gwlx, xl):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '城市', '学历', '岗位描述'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == gwlx]
    data = data[data['城市'] == city]
    data = data[data['学历'] == xl]
    s = ""
    for i in list(data['岗位描述']):
        s += i
    _k = keys(s)
    _w = weights(s)
    s = []
    for i in range(len(_k)):
        s.append({
            "name": _k[i],
            "value": _w[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<city>/<gwlx>/<xl>/技能需求')
def div1xq(city, gwlx, xl):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '城市', '学历', '技能需求'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == gwlx]
    data = data[data['城市'] == city]
    data = data[data['学历'] == xl]
    s = ""
    for i in list(data['技能需求']):
        s += i
    _k = keys(s)
    _w = weights(s)
    s = []
    for i in range(len(_k)):
        s.append({
            "name": _k[i],
            "value": _w[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<gwlx>/div2')
def div2(gwlx):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '学历'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == gwlx]
    s = []
    for i in list(data['学历'].unique()):
        s.append({
            "name": i,
            "招聘信息数量": counts(list(data[data['学历'] == i]['学历']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<gwlx>/div3')
def div3(gwlx):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '城市'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == gwlx]
    s = []
    for i in list(data['城市'].unique()):
        s.append({
            "name": i,
            "招聘信息数量": counts(list(data[data['城市'] == i]['城市']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<city>/div4')
def div4(city):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '城市', '学历等级', '平均薪资', '学历'])
    data = data.dropna(axis=0, how='any')
    data = data[data['城市'] == city]
    data = data.sort_values(by=['学历等级'])
    s = []
    学历 = list(data['学历'].unique())
    岗位类型 = list(data['岗位类型'].unique())
    for i in 学历:
        for j in 岗位类型:
            _data = data[data['学历'] == i]
            _data = _data[_data['岗位类型'] == j]
            s.append({
                "name": j,
                "type": i,
                "平均薪资": avr(list(_data['平均薪资']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<zy>/div5')
def div5(zy):
    data = pd.read_csv('data/zyGwlxRatio.csv')
    data = data[data['专业类'] == zy]
    nodes = [{
        "name": zy
    }]
    links = []
    for i in list(data['岗位类型'].unique()):
        _data = data[data['岗位类型'] == i]
        nodes.append({
            "name": i
        })
        links.append({
            "source": zy,
            "target": i,
            "value": avr(list(_data['关联度']))
        })
    s = {
        "nodes": nodes,
        "links": links
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<edu>/<city>/<gwlx>/<xb>/<age>/<zy>/<gzjy>/div6')
def div6(edu, city, gwlx, xb, age, zy, gzjy):
    data = pd.read_csv('data/zpxx.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['学历'] == edu]
    data = data[data['工作经验'] == gzjy]
    data = data[data['城市'] == city]
    data = data[data['岗位类型'] == gwlx]
    data = data.sort_values(by=['平均薪资'], ascending=False)
    s = []
    岗位类型 = list(data['岗位类型'])
    岗位名称 = list(data['岗位名称'])
    薪资 = list(data['薪资'])
    城市 = list(data['城市'])
    工作经验 = list(data['工作经验'])
    学历 = list(data['学历'])
    工作类型 = list(data['工作类型'])
    招聘人数 = list(data['招聘人数'])
    公司名称 = list(data['公司名称'])
    技能需求 = list(data['技能需求'])
    岗位描述 = list(data['岗位描述'])
    for i in range(min(30, len(城市))):
        d1 = pd.read_csv('data/zyGwlxRatio.csv')
        d1 = d1[d1['岗位类型'] == 岗位类型[i]]
        d1 = d1[d1['专业类'] == zy]
        d1 = list(d1['关联度'])[0]
        d2 = pd.read_csv('data/nlGwlxRatio.csv')
        d2 = d2[d2['岗位类型'] == 岗位类型[i]]
        d2 = round(1 - (list(d2['最佳年龄'])[0] - int(age)) / 50, 2)
        d3 = pd.read_csv('data/xbGwlxRatio.csv')
        d3 = d3[d3['岗位类型'] == 岗位类型[i]]
        d3 = d3[d3['性别'] == xb]
        d3 = list(d3['关联度'])[0]
        s.append({
            "岗位名称": 岗位名称[i],
            "岗位类型": 岗位类型[i],
            "工作经验": 工作经验[i],
            "工作类型": 工作类型[i],
            "公司名称": 公司名称[i],
            "招聘人数": 招聘人数[i],
            "学历": 学历[i],
            "城市": 城市[i],
            "薪资": 薪资[i],
            "技能需求": 技能需求[i],
            "岗位描述": 岗位描述[i],
            "匹配度": round((d1 + d2 + d3) / 3, 2)
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<xb>/<age>/<edu>/<zy>/<gzjy>/div6')
def div6_(xb, age, edu, zy, gzjy):
    try:
        data = pd.read_csv('data/zpxx.csv')
        data = data.dropna(axis=0, how='any')
        data = data[data['学历'] == edu]
        data = data[data['工作经验'] == gzjy]
        d1 = pd.read_csv('data/zyGwlxRatio.csv').sort_values(by=['关联度'], ascending=False)
        d1 = d1[d1['专业类'] == zy]
        gwlx = list(d1['岗位类型'])[0]
        data = data[data['岗位类型'] == gwlx]
        data = data.sort_values(by=['平均薪资'], ascending=False)
        s = []
        岗位类型 = list(data['岗位类型'])
        岗位名称 = list(data['岗位名称'])
        薪资 = list(data['薪资'])
        城市 = list(data['城市'])
        工作经验 = list(data['工作经验'])
        学历 = list(data['学历'])
        工作类型 = list(data['工作类型'])
        招聘人数 = list(data['招聘人数'])
        公司名称 = list(data['公司名称'])
        技能需求 = list(data['技能需求'])
        岗位描述 = list(data['岗位描述'])
        for i in range(min(100, len(城市))):
            d1 = pd.read_csv('data/zyGwlxRatio.csv')
            d1 = d1[d1['岗位类型'] == 岗位类型[i]]
            d1 = d1[d1['专业类'] == zy]
            d1 = list(d1['关联度'])[0]
            d2 = pd.read_csv('data/nlGwlxRatio.csv')
            d2 = d2[d2['岗位类型'] == 岗位类型[i]]
            d2 = round(1 - (list(d2['最佳年龄'])[0] - int(age)) / 50, 2)
            d3 = pd.read_csv('data/xbGwlxRatio.csv')
            d3 = d3[d3['岗位类型'] == 岗位类型[i]]
            d3 = d3[d3['性别'] == xb]
            d3 = list(d3['关联度'])[0]
            s.append({
                "岗位名称": 岗位名称[i],
                "岗位类型": 岗位类型[i],
                "工作经验": 工作经验[i],
                "工作类型": 工作类型[i],
                "公司名称": 公司名称[i],
                "招聘人数": 招聘人数[i],
                "学历": 学历[i],
                "城市": 城市[i],
                "薪资": 薪资[i],
                "技能需求": 技能需求[i],
                "岗位描述": 岗位描述[i],
                "匹配度": round((d1 + d2 + d3) / 3, 2)
            })
        s = pd.DataFrame(s).sort_values(by=['匹配度'], ascending=False)
        data = s
        s = []
        岗位类型 = list(data['岗位类型'])
        岗位名称 = list(data['岗位名称'])
        薪资 = list(data['薪资'])
        城市 = list(data['城市'])
        工作经验 = list(data['工作经验'])
        学历 = list(data['学历'])
        工作类型 = list(data['工作类型'])
        招聘人数 = list(data['招聘人数'])
        公司名称 = list(data['公司名称'])
        技能需求 = list(data['技能需求'])
        岗位描述 = list(data['岗位描述'])
        匹配度 = list(data['匹配度'])
        for i in range(min(100, len(城市))):
            s.append({
                "岗位名称": 岗位名称[i],
                "岗位类型": 岗位类型[i],
                "工作经验": 工作经验[i],
                "工作类型": 工作类型[i],
                "公司名称": 公司名称[i],
                "招聘人数": 招聘人数[i],
                "学历": 学历[i],
                "城市": 城市[i],
                "薪资": 薪资[i],
                "技能需求": 技能需求[i],
                "岗位描述": 岗位描述[i],
                "匹配度": 匹配度[i]
            })
        d1 = pd.read_csv('data/zyGwlxRatio.csv').sort_values(by=['关联度'], ascending=False)
        d1 = d1[d1['专业类'] == zy]
        gwlx = list(d1['岗位类型'])[0]
        return jsonify(json.loads(_json({
            "data": s,
            "gwlx": gwlx
        })))
    except:
        data = pd.read_csv('data/zpxx.csv')
        data = data.dropna(axis=0, how='any')
        data = data[data['学历'] == edu]
        d1 = pd.read_csv('data/zyGwlxRatio.csv').sort_values(by=['关联度'], ascending=False)
        data = data.sort_values(by=['平均薪资'], ascending=False)
        s = []
        岗位类型 = list(data['岗位类型'])
        岗位名称 = list(data['岗位名称'])
        薪资 = list(data['薪资'])
        城市 = list(data['城市'])
        工作经验 = list(data['工作经验'])
        学历 = list(data['学历'])
        工作类型 = list(data['工作类型'])
        招聘人数 = list(data['招聘人数'])
        公司名称 = list(data['公司名称'])
        技能需求 = list(data['技能需求'])
        岗位描述 = list(data['岗位描述'])
        for i in range(min(100, len(城市))):
            d1 = pd.read_csv('data/zyGwlxRatio.csv')
            d1 = d1[d1['岗位类型'] == 岗位类型[i]]
            d1 = d1[d1['专业类'] == zy]
            d1 = list(d1['关联度'])[0]
            d2 = pd.read_csv('data/nlGwlxRatio.csv')
            d2 = d2[d2['岗位类型'] == 岗位类型[i]]
            d2 = round(1 - (list(d2['最佳年龄'])[0] - int(age)) / 50, 2)
            d3 = pd.read_csv('data/xbGwlxRatio.csv')
            d3 = d3[d3['岗位类型'] == 岗位类型[i]]
            d3 = d3[d3['性别'] == xb]
            d3 = list(d3['关联度'])[0]
            s.append({
                "岗位名称": 岗位名称[i],
                "岗位类型": 岗位类型[i],
                "工作经验": 工作经验[i],
                "工作类型": 工作类型[i],
                "公司名称": 公司名称[i],
                "招聘人数": 招聘人数[i],
                "学历": 学历[i],
                "城市": 城市[i],
                "薪资": 薪资[i],
                "技能需求": 技能需求[i],
                "岗位描述": 岗位描述[i],
                "匹配度": round((d1 + d2 + d3) / 3, 2)
            })
        s = pd.DataFrame(s).sort_values(by=['匹配度'], ascending=False)
        data = s
        s = []
        岗位类型 = list(data['岗位类型'])
        岗位名称 = list(data['岗位名称'])
        薪资 = list(data['薪资'])
        城市 = list(data['城市'])
        工作经验 = list(data['工作经验'])
        学历 = list(data['学历'])
        工作类型 = list(data['工作类型'])
        招聘人数 = list(data['招聘人数'])
        公司名称 = list(data['公司名称'])
        技能需求 = list(data['技能需求'])
        岗位描述 = list(data['岗位描述'])
        匹配度 = list(data['匹配度'])
        for i in range(min(100, len(城市))):
            s.append({
                "岗位名称": 岗位名称[i],
                "岗位类型": 岗位类型[i],
                "工作经验": 工作经验[i],
                "工作类型": 工作类型[i],
                "公司名称": 公司名称[i],
                "招聘人数": 招聘人数[i],
                "学历": 学历[i],
                "城市": 城市[i],
                "薪资": 薪资[i],
                "技能需求": 技能需求[i],
                "岗位描述": 岗位描述[i],
                "匹配度": 匹配度[i]
            })
        d1 = pd.read_csv('data/zyGwlxRatio.csv').sort_values(by=['关联度'], ascending=False)
        d1 = d1[d1['专业类'] == zy]
        gwlx = list(d1['岗位类型'])[0]
        return jsonify(json.loads(_json({
            "data": s,
            "gwlx": gwlx
        })))


@app.route('/div603')
def div603():
    data = pd.read_csv('data/faceSucesss.csv')
    时间 = list(data['时间'])
    姓名 = list(data['姓名'])
    性别 = list(data['性别'])
    专业类 = list(data['专业类'])
    岗位类型 = list(data['岗位类型'])
    面试预约 = list(data['面试预约'])
    面试通过 = list(data['面试通过'])
    s = []
    for i in range(len(时间)):
        s.append({
            "时间": 时间[i],
            "姓名": 姓名[i],
            '性别': 性别[i],
            "专业类": 专业类[i],
            "岗位类型": 岗位类型[i],
            "面试预约": 面试预约[i],
            "面试通过": 面试通过[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<city>/<gwlx>/div7')
def div7(city, gwlx):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '城市', '学历等级', '平均薪资', '学历', '工作经验等级', '工作经验'])
    data = data.dropna(axis=0, how='any')
    data = data[data['城市'] == city]
    data = data[data['岗位类型'] == gwlx]
    s = []
    data = data.sort_values(by=['学历等级'])
    for i in list(data['学历'].unique()):
        data = data.sort_values(by=['工作经验等级'])
        for j in list(data['工作经验'].unique()):
            _data = data[data['学历'] == i]
            _data = _data[_data['工作经验'] == j]
            s.append({
                "学历": i,
                "工作经验": j,
                "平均薪资": avr(list(_data['平均薪资']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<gwlx>/<xl>/div8')
def div8(gwlx, xl):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '平均薪资', '工作经验等级', '工作经验', '学历'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == gwlx]
    data = data[data['学历'] == xl]
    data = data.sort_values(by=['工作经验等级'])
    s = []
    for i in list(data['工作经验'].unique()):
        if avr(list(data[data['工作经验'] == i]['平均薪资'])) == 0 and list(data['工作经验'].unique()).index(i) != 0:
            s.append({
                "工作经验": i,
                "平均薪资": avr(list(data[data['工作经验'] == list(data['工作经验'].unique())[
                    list(data['工作经验'].unique()).index(i) - 1
                    ]]['平均薪资'])) * 1.1
            })
        else:
            s.append({
                "工作经验": i,
                "平均薪资": avr(list(data[data['工作经验'] == i]['平均薪资']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/city')
def city(x, y):
    data = pd.read_csv('data/zpxx.csv', usecols=['城市', '经度', '纬度'])
    城市 = list(data['城市'].unique())
    经度 = list(data['经度'].unique())
    纬度 = list(data['纬度'].unique())
    minI = 0
    minDis = 100000
    for i in range(len(城市)):
        if pow(float(经度[i]) - float(x), 2) + pow(float(纬度[i]) - float(y), 2) < minDis:
            minI = i
            minDis = pow(float(经度[i]) - float(x), 2) + pow(float(纬度[i]) - float(y), 2)
    return jsonify(json.loads(_json({
        "city": 城市[minI]
    })))


@app.route('/<gwlx>/l1_2')
def l1_2(gwlx):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '平均薪资', '经度', '纬度'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == gwlx]
    s = []
    jd = list(data['经度'].unique())
    wd = list(data['纬度'].unique())
    for i in range(len(jd)):
        _data = data[data['经度'] == jd[i]]
        _data = _data[_data['纬度'] == wd[i]]
        s.append({
            "jd": jd[i],
            "wd": wd[i],
            "value1": avr(list(_data['平均薪资'])),
            "value2": counts(list(_data['经度'])),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<gwlx>/<xl>/l3_4')
def l3_4(gwlx, xl):
    data = pd.read_csv('data/zpxx.csv', usecols=['学历', '平均薪资', '经度', '纬度', '岗位类型'])
    data = data.dropna(axis=0, how='any')
    data = data[data['学历'] == xl]
    data = data[data['岗位类型'] == gwlx]
    s = []
    jd = list(data['经度'].unique())
    wd = list(data['纬度'].unique())
    for i in range(len(jd)):
        _data = data[data['经度'] == jd[i]]
        _data = _data[_data['纬度'] == wd[i]]
        s.append({
            "jd": jd[i],
            "wd": wd[i],
            "value1": avr(list(_data['平均薪资'])),
            "value2": counts(list(_data['经度'])),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<gwlx>/zpsj')
def p4_zpsj(gwlx):
    data = pd.read_csv('data/zpxx.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == gwlx]
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(min(len(L[0]), 30)):
        _s = {}
        for j in range(len(L)):
            _s.update({
                headers[j]: L[j][i]
            })
        s.append(_s)
    columns = []
    for header in headers:
        if header != "岗位描述":
            columns.append({
                "prop": header,
                "label": header,
                "width": "150"
            })
    s = {
        "data": s,
        "columns": columns
    }
    return jsonify(json.loads(_json(s)))


def zyGwlxRatio():
    data1 = pd.read_csv('data/gwlx.csv')
    data2 = pd.read_csv('data/zy.csv')
    s = []
    for i in list(data1[list(data1.head(0))[0]]):
        for j in list(data2[list(data2.head(0))[0]]):
            s.append({
                "岗位类型": i,
                "专业类": j,
                "关联度": 0.5
            })
    pd.DataFrame(s).to_csv('data/zyGwlxRatio.csv', index=0)


def xbGwlxRatio():
    data1 = pd.read_csv('data/gwlx.csv')
    s = []
    for i in list(data1[list(data1.head(0))[0]]):
        for j in ['男', '女']:
            s.append({
                "岗位类型": i,
                "性别": j,
                "关联度": 0.5
            })
    pd.DataFrame(s).to_csv('data/xbGwlxRatio.csv', index=0)


@app.route('/mssj')
def mssj():
    data = pd.read_csv('data/faceSucesss.csv')
    data = data.dropna(axis=0, how='any')
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(5):
        _s = {}
        for j in range(len(L)):
            _s.update({
                headers[j]: L[j][i]
            })
        s.append(_s)
    columns = []
    for header in headers:
        columns.append({
            "prop": header,
            "label": header,
            "width": "150"
        })
    s = {
        "data": s,
        "columns": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/zpsj')
def zpsj():
    data = pd.read_csv('data/zpxx.csv')
    data = data.dropna(axis=0, how='any')
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(100):
        _s = {}
        for j in range(len(L)):
            _s.update({
                headers[j]: L[j][i]
            })
        s.append(_s)
    columns = []
    for header in headers:
        if header != "岗位描述":
            columns.append({
                "prop": header,
                "label": header,
                "width": "150"
            })
    s = {
        "data": s,
        "columns": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/gssj')
def gssj():
    data = pd.read_csv('data/company.csv')
    data = data.dropna(axis=0, how='any')
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(20):
        _s = {}
        for j in range(len(L)):
            _s.update({
                headers[j]: L[j][i]
            })
        s.append(_s)
    columns = []
    for header in headers:
        columns.append({
            "prop": header,
            "label": header,
            "width": "250"
        })
    s = {
        "data": s,
        "columns": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/company/zpsj')
def zpsj_company(x):
    data = pd.read_csv('data/zpxx.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['公司名称'] == x]
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(min(len(L[0]), 100)):
        _s = {}
        for j in range(len(L)):
            _s.update({
                headers[j]: L[j][i]
            })
        s.append(_s)
    columns = []
    for header in headers:
        if header != "岗位描述":
            columns.append({
                "prop": header,
                "label": header,
                "width": 150
            })
    s = {
        "data": s,
        "columns": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<jd>/<wd>/d201')
def d201(x, jd, wd):
    data = pd.read_csv('data/zpxx.csv', usecols=['公司名称', '岗位类型', '岗位名称', '城市', '平均薪资', '工作经验', '经度', '纬度'])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == x]
    jd = float(jd)
    wd = float(wd)
    nodes = []
    links = []
    categories = []
    for c in list(data['工作经验'].unique()):
        categories.append({
            "name": c
        })
    a = 0
    for i in list(data['公司名称'].unique()):
        a += 1
        _data = data[data['公司名称'] == i]
        nodes.append({
            "id": str(a),
            "name": i.replace(",", "").replace("，", "").replace("'", ""),
            "symbolSize": min(counts(list(_data['平均薪资'])), 50),
            "x": (jd - avr(list(_data['经度'])) + random.random() * 0.5) * 300000,
            "y": (wd - avr(list(_data['纬度'])) + random.random() * 0.5) * 200000,
            "value": avr(list(_data['平均薪资'])),
            "category": list(data['工作经验'].unique()).index(list(_data['工作经验'])[0])
        })
        b = a
        for j in list(_data['岗位名称'].unique()):
            b += 1
            __data = _data[_data['岗位名称'] == j]
            nodes.append({
                "id": str(b),
                "name": j.replace(",", "").replace("，", "").replace("'", ""),
                "symbolSize": min(counts(list(__data['平均薪资'])), 50),
                "x": (jd - avr(list(__data['经度'])) + random.random() * 0.2) * 60000,
                "y": (wd - avr(list(__data['纬度'])) + random.random() * 0.2) * 40000,
                "value": avr(list(__data['平均薪资'])),
                "category": list(data['工作经验'].unique()).index(list(__data['工作经验'])[0])
            })
            links.append({
                "source": str(a),
                "target": str(b)
            })
        a = b
    s = {
        "nodes": nodes,
        "links": links,
        "categories": categories
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d202')
def d202(x, y):
    data = pd.read_csv('data/zpxx.csv',
                       usecols=[
                           '岗位类型',
                           '城市',
                           '平均薪资',
                           '工作经验',
                           '学历'
                       ])
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == x]
    _data = data[data['城市'] == y]
    s = []
    for j in ['不限', '无经验', '1年以下', '1-3年', '3-5年', '5-10年']:
        __data = _data[_data['工作经验'] == j]
        for k in ['学历不限', '初中及以下', '中专/中计', '中计', '高中', '大专', '本科', '硕士', 'MBA/EMBA', '博士']:
            ___data = __data[__data['学历'] == k]
            s.append({
                "source": j.replace(",", "").replace("，", "").replace("'", ""),
                "target": k.replace(",", "").replace("，", "").replace("'", ""),
                "value": avr(list(___data['平均薪资']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d203')
def d203(x):
    data = pd.read_csv('data/zpxx.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['岗位类型'] == x]
    s = []
    for i in list(data['工作类型'].unique()):
        _data = data[data['工作类型'] == i]
        for j in ['不限', '无经验', '1年以下', '1-3年', '3-5年', '5-10年']:
            __data = _data[_data['工作经验'] == j]
            s.append({
                "source": i.replace(",", "").replace("，", "").replace("'", ""),
                "target": j.replace(",", "").replace("，", "").replace("'", ""),
                "value": sums(list(__data['招聘人数']))
            })
            for k in ['学历不限', '初中及以下', '中专/中计', '中计', '高中', '大专', '本科', '硕士', 'MBA/EMBA', '博士']:
                ___data = __data[__data['学历'] == k]
                s.append({
                    "source": j.replace(",", "").replace("，", "").replace("'", ""),
                    "target": k.replace(",", "").replace("，", "").replace("'", ""),
                    "value": sums(list(___data['招聘人数']))
                })
                for ii in list(data['城市'].unique()):
                    ____data = ___data[___data['城市'] == ii]
                    s.append({
                        "source": k.replace(",", "").replace("，", "").replace("'", ""),
                        "target": ii.replace(",", "").replace("，", "").replace("'", ""),
                        "value": sums(list(____data['招聘人数']))
                    })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d2041')
def d2041(x):
    data = pd.read_csv('data/zpxx.csv', usecols=['公司名称', '岗位描述'])
    data = data[data['公司名称'] == x]
    s = ""
    for c in list(data['岗位描述'].unique())[:20]:
        s += c
    _k = keys(s)
    _w = weights(s)
    s = []
    for i in range(len(_k)):
        s.append({
            "name": _k[i],
            "value": _w[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d2042')
def d2042(x):
    data = pd.read_csv('data/zpxx.csv', usecols=['公司名称', '技能需求'])
    data = data[data['公司名称'] == x]
    s = ""
    for c in list(data['技能需求'].unique())[:20]:
        s += c
    _k = keys(s)
    _w = weights(s)
    s = []
    for i in range(len(_k)):
        s.append({
            "name": _k[i],
            "value": _w[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d2043')
def d2043(x, y):
    data = pd.read_csv('data/zpxx.csv', usecols=['公司名称', '岗位类型', '技能需求', '岗位描述', '岗位名称', '平均薪资'])
    data = data[data['岗位类型'] == x]
    data = data[data['公司名称'] == y]
    nl = avr(
        list(pd.read_csv('data/nlGwlxRatio.csv')[
                 pd.read_csv('data/nlGwlxRatio.csv')['岗位类型'] == x
                 ]['最佳年龄'])
    )
    zyR = pd.read_csv('data/zyGwlxRatio.csv')
    zyR = zyR[zyR['岗位类型'] == x]
    zyR = zyR.sort_values(by=['关联度'], ascending=False)
    zy = list(zyR['专业类'])[:3]
    xbR = pd.read_csv('data/xbGwlxRatio.csv')
    xbR = xbR[xbR['岗位类型'] == x]
    xbR = xbR.sort_values(by=['关联度'], ascending=False)
    xb = list(xbR['性别'])[0]
    岗位名称 = list(data['岗位名称'])
    s1 = x + "这一岗位, 从面试数据中可分析得出，面试者中" + xb + "性居多。"
    s2 = "最佳的就业年龄是：" + str(nl - 5) + "~" + str(nl + 5) + "岁。"
    s3 = "匹配度最高的专业为：" + zy[0] + "," + zy[1] + "," + zy[2] + "。"
    s4 = "在" + y + "中有" + str(len(岗位名称)) + "个与" + x + "相关的岗位正在进行招聘"
    s5 = "平均薪资在" + str(avr(list(data['平均薪资']))) + "元"
    return jsonify(json.loads(
        _json({
            "value1": s1,
            "value2": s2,
            "value3": s3,
            "value4": s4,
            "value5": s5,
        })
    ))


@app.route('/<x>/<y>/<z>/<types>/d301')
def d301(x, y, z, types):
    data = pd.read_csv('data/zpxx.csv', usecols=['城市', '岗位类型', '学历', '工作经验', '平均薪资'])
    data = data[data['岗位类型'] == z]
    data1 = data[data['城市'] == x]
    data2 = data[data['城市'] == y]
    s = []
    for i in list(data[types].unique()):
        _data1 = data1[data1[types] == i]
        _data2 = data2[data2[types] == i]
        s.append({
            "name": i,
            x: avr(list(_data1['平均薪资'])),
            y: avr(list(_data2['平均薪资']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<types>/d302')
def d302(x, types):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '学历', '工作经验', '平均薪资', '公司名称'])
    data = data[data['岗位类型'] == x]
    s = []
    for i in list(data['公司名称'].unique()):
        for j in list(data[types].unique()):
            _data = data[data['公司名称'] == i]
            _data = _data[_data[types] == j]
            s.append({
                "name": i.replace("'", ""),
                "type": j,
                "value": counts(list(_data['平均薪资']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d303_4')
def d303_4(x, y):
    data = pd.read_csv('data/zpxx.csv', usecols=['岗位类型', '学历', '工作经验', '平均薪资', '公司名称'])
    data = data[data['岗位类型'] == x]
    data = data[data['公司名称'] == y]
    s = []
    for i in ['学历不限', '初中及以下', '中专/中计', '中计', '高中', '大专', '本科', '硕士', 'MBA/EMBA', '博士']:
        for j in ['不限', '无经验', '1年以下', '1-3年', '3-5年', '5-10年']:
            _data = data[data['学历'] == i]
            _data = _data[_data['工作经验'] == j]
            s.append({
                "name": i,
                "type": j,
                "value": avr(list(_data['平均薪资']))
            })
    return jsonify(json.loads(_json(s)))


app.run(host='127.0.0.1', port=1500, debug=True)
