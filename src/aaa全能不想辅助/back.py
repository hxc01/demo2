import os
import math
import json
import jieba
import random
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import date


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


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/layer1')
def p1layer1():
    data = pd.read_csv('result/养老机构.csv')
    data = data.dropna(axis=0, how='any')
    s = []
    机构名称 = list(data['机构名称'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    机构类别 = list(data['机构类别'])
    运营方式 = list(data['运营方式'])
    兴办主体 = list(data['兴办主体'])
    床位总数 = list(data['床位总数'])
    护理型床位数 = list(data['护理型床位数'])
    入住老年人数 = list(data['入住老年人数'])
    从业人员数 = list(data['从业人员数'])
    for i in range(len(机构名称)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "床位总数": int(床位总数[i]),
            "入住老年人数": int(入住老年人数[i]),
            "从业人员数": int(从业人员数[i]),
            "机构名称": 机构名称[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/layer2')
def p1layer2():
    data = pd.read_csv('result/小区养老设施.csv')
    data = data.dropna(axis=0, how='any')
    s = []
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    住户人数 = list(data['住户人数'])
    建筑面积 = list(data['建筑面积'])
    小区名称 = list(data['小区名称'])
    for i in range(len(经度)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "住户人数": 住户人数[i],
            "建筑面积": 建筑面积[i],
            "小区名称": 小区名称[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/layer3')
def p1layer3():
    data = pd.read_csv('result/日间照料中心.csv')
    data = data.dropna(axis=0, how='any')
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    建筑面积 = list(data['建筑面积'])
    床位数量 = list(data['床位数量'])
    机构名称 = list(data['机构名称'])
    s = []
    for i in range(len(经度)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "建筑面积": int(建筑面积[i]),
            "床位数量": int(床位数量[i]),
            "机构名称": 机构名称[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/layer4')
def p1layer4():
    data = pd.read_csv('result/幸福院.csv')
    data = data.dropna(axis=0, how='any')
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    建筑面积 = list(data['建筑面积'])
    床位数量 = list(data['床位数量'])
    机构名称 = list(data['机构名称'])
    s = []
    for i in range(len(经度)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "建筑面积": 建筑面积[i],
            "床位数量": 床位数量[i],
            "机构名称": 机构名称[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/layer5')
def p1layer5():
    data = pd.read_csv('result/助餐点.csv')
    data = data.dropna(axis=0, how='any')
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    建筑面积 = list(data['建筑面积'])
    机构名称 = list(data['机构名称'])
    s = []
    for i in range(len(经度)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "建筑面积": 建筑面积[i],
            "机构名称": 机构名称[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<name>/div1')
def p1div1(name):
    data = pd.read_csv('result/养老机构.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['机构名称'] == name]
    s = []
    机构名称 = list(data['机构名称'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    机构类别 = list(data['机构类别'])
    运营方式 = list(data['运营方式'])
    兴办主体 = list(data['兴办主体'])
    床位总数 = list(data['床位总数'])
    护理型床位数 = list(data['护理型床位数'])
    入住老年人数 = list(data['入住老年人数'])
    从业人员数 = list(data['从业人员数'])
    for i in range(len(机构名称)):
        s.append({
            "床位总数": int(床位总数[i]),
            "入住老年人数": int(入住老年人数[i]),
            "从业人员数": int(从业人员数[i]),
            "机构名称": 机构名称[i],
            "机构类别": 机构类别[i],
            "运营方式": 运营方式[i],
            "兴办主体": 兴办主体[i],
            "护理型床位数": 护理型床位数[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<name>/div2')
def p1div2(name):
    data = pd.read_csv('result/小区养老设施.csv')
    data = data[data['小区名称'] == name]
    data = data.dropna(axis=0, how='any')
    机构名称 = list(data['机构名称'])
    住户人数 = list(data['住户人数'])
    建筑面积 = list(data['建筑面积'])
    街道名称 = list(data['街道名称'])
    小区名称 = list(data['小区名称'])
    s = []
    for i in range(len(机构名称)):
        s.append({
            "机构名称": 机构名称[i],
            "住户人数": 住户人数[i],
            "建筑面积": 建筑面积[i],
            "街道名称": 街道名称[i],
            "小区名称": 小区名称[i],
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<name>/div3')
def p1div3(name):
    data = pd.read_csv('result/日间照料中心.csv')
    data = data[data['机构名称'] == name]
    data = data.dropna(axis=0, how='any')
    县市区 = list(data['县市区'])
    地址 = list(data['地址'])
    建筑面积 = list(data['建筑面积'])
    床位数量 = list(data['床位数量'])
    运营性质 = list(data['运营性质'])
    机构名称 = list(data['机构名称'])
    s = []
    for i in range(len(机构名称)):
        s.append({
            "机构名称": 机构名称[i],
            "县市区": 县市区[i],
            "地址": 地址[i],
            "建筑面积": int(建筑面积[i]),
            "床位数量": int(床位数量[i]),
            "运营性质": 运营性质[i],
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<name>/div4')
def p1div4(name):
    data = pd.read_csv('result/幸福院.csv')
    data = data[data['机构名称'] == name]
    data = data.dropna(axis=0, how='any')
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    建筑面积 = list(data['建筑面积'])
    床位数量 = list(data['床位数量'])
    机构名称 = list(data['机构名称'])
    运营性质 = list(data['运营性质'])
    s = []
    for i in range(len(经度)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "建筑面积": 建筑面积[i],
            "床位数量": 床位数量[i],
            "机构名称": 机构名称[i],
            "运营性质": 运营性质[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<csvName>/<lng1>/<lng2>/<lat1>/<lat2>/bar1')
def p1bar1(csvName, lng1, lng2, lat1, lat2):
    data = pd.read_csv('result/' + csvName + "矩阵.csv")
    data = data.dropna(axis=0, how='any')
    value = '分数'
    valueName = value
    value = list(data[value])
    name = list(data[list(data.head(0))[0]])
    jd = list(data['经度'])
    wd = list(data['纬度'])
    s = []
    for i in range(len(value)):
        if min(float(lng1), float(lng2)) <= jd[i] <= max(float(lng1), float(lng2)):
            if min(float(lat1), float(lat2)) <= wd[i] <= max(float(lat1), float(lat2)):
                s.append({
                    "name": name[i],
                    "value": value[i],
                    "jd": jd[i],
                    "wd": wd[i]
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<csvName>/<value>/<lng1>/<lng2>/<lat1>/<lat2>/pie1')
def p1pie1(csvName, value, lng1, lng2, lat1, lat2):
    data = pd.read_csv('result/' + csvName + ".csv")
    data = data.dropna(axis=0, how='any')
    valueName = value
    value = list(data[value].unique())
    values = list(data[valueName])
    name = list(data[list(data.head(0))[0]])
    jd = list(data['经度'])
    wd = list(data['纬度'])
    s = {}
    for i in range(len(value)):
        s.update({
            value[i]: 0
        })
    for i in range(len(values)):
        if min(float(lng1), float(lng2)) <= jd[i] <= max(float(lng1), float(lng2)):
            if min(float(lat1), float(lat2)) <= wd[i] <= max(float(lat1), float(lat2)):
                s[values[i]] += 1
    _s = []
    for c in s:
        _s.append({
            "name": c,
            "value": s[c]
        })
    return jsonify(json.loads(_json(_s)))


@app.route('/<csvName>/<value1>/<value2>/<lng1>/<lng2>/<lat1>/<lat2>/column1')
def p1column1(csvName, value1, value2, lng1, lng2, lat1, lat2):
    data = pd.read_csv('result/' + csvName + ".csv")
    data = data.dropna(axis=0, how='any')
    value1Name = value1
    value2Name = value2
    nameName = list(data.head(0))[0]
    name = list(data[nameName])
    jd = list(data['经度'])
    wd = list(data['纬度'])
    value1 = list(data[value1])
    value2 = list(data[value2])
    s = []
    for i in range(len(name)):
        if min(float(lng1), float(lng2)) <= jd[i] <= max(float(lng1), float(lng2)):
            if min(float(lat1), float(lat2)) <= wd[i] <= max(float(lat1), float(lat2)):
                s.append({
                    "name": name[i],
                    "value": value1[i],
                    "type": value1Name,
                    "jd": jd[i],
                    "wd": wd[i]
                })
                s.append({
                    "name": name[i],
                    "value": value2[i],
                    "type": value2Name,
                    "jd": jd[i],
                    "wd": wd[i]
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<a1>/<a2>/<a3>/<a4>/<a5>/<a6>/reviewIn')
def reviewIn(a1, a2, a3, a4, a5, a6):
    data = pd.read_csv('out/评价数据集.csv')
    s = []
    机构名称 = list(data['机构名称'])
    环境评分 = list(data['环境评分'])
    设施评分 = list(data['设施评分'])
    服务评分 = list(data['服务评分'])
    伙食评分 = list(data['伙食评分'])
    文字评价 = list(data['文字评价'])
    for i in range(len(机构名称)):
        s.append({
            "机构名称": 机构名称[i],
            "环境评分": 环境评分[i],
            "设施评分": 设施评分[i],
            "服务评分": 服务评分[i],
            "伙食评分": 伙食评分[i],
            "文字评价": 文字评价[i],
        })
    s.append({
        "机构名称": a1,
        "环境评分": a2,
        "设施评分": a3,
        "服务评分": a4,
        "伙食评分": a5,
        "文字评价": a6,
    })
    pd.DataFrame(s).to_csv('out/评价数据集.csv', index=0)
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/reviewWords')
def reviewWords(x):
    data = pd.read_csv('out/评价数据集.csv')
    data = data[data['机构名称'] == x]
    文字评价 = list(data['文字评价'])
    s = ""
    for c in 文字评价:
        s += c
    _key = keys(s)
    _wei = weights(s)
    s = []
    for i in range(len(_key)):
        s.append({
            "name": _key[i],
            "value": _wei[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/reviewScores')
def reviewScores(x):
    data = pd.read_csv('out/评价数据集.csv')
    data = data[data['机构名称'] == x]
    s = [
        {
            "name": "环境评分",
            "value": int(round(avr(list(data['环境评分'])), 0))
        },
        {
            "name": "设施评分",
            "value": int(round(avr(list(data['设施评分'])), 0))
        },
        {
            "name": "服务评分",
            "value": int(round(avr(list(data['服务评分'])), 0))
        },
        {
            "name": "伙食评分",
            "value": int(round(avr(list(data['伙食评分'])), 0))
        }
    ]
    return jsonify(json.loads(_json(s)))


@app.route('/<name>/div1')
def div501(name):
    data = pd.read_csv('result/养老机构.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['机构名称'] == name]
    s = []
    机构名称 = list(data['机构名称'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    机构类别 = list(data['机构类别'])
    运营方式 = list(data['运营方式'])
    兴办主体 = list(data['兴办主体'])
    床位总数 = list(data['床位总数'])
    护理型床位数 = list(data['护理型床位数'])
    入住老年人数 = list(data['入住老年人数'])
    从业人员数 = list(data['从业人员数'])
    for i in range(len(机构名称)):
        s.append({
            "床位总数": int(床位总数[i]),
            "入住老年人数": int(入住老年人数[i]),
            "从业人员数": int(从业人员数[i]),
            "机构名称": 机构名称[i],
            "机构类别": 机构类别[i],
            "运营方式": 运营方式[i],
            "兴办主体": 兴办主体[i],
            "护理型床位数": 护理型床位数[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<code>/<password>/checkUser1')
def checkUser1(code, password):
    data = pd.read_csv('out/用户信息表.csv')
    data = data[data['code'] == code]
    if str(password) == str(list(data['password'])[0]):
        return jsonify(json.loads(_json(
            {
                "value": 1
            }
        )))
    else:
        return jsonify(json.loads(_json(
            {
                "value": 0
            }
        )))


@app.route('/<code>/<password>/regisUser1')
def regisUser1(code, password):
    data = pd.read_csv('out/用户信息表.csv')
    data = data[data['code'] == code]
    if len(list(data['code'])):
        return jsonify(json.loads(_json(
            {
                "value": 0
            }
        )))
    else:
        data = pd.read_csv('out/用户信息表.csv')
        s = []
        codes = list(data['code'])
        passwords = list(data['password'])
        for i in range(len(codes)):
            s.append({
                "code": codes[i],
                "password": passwords[i]
            })
        s.append({
            "code": code,
            "password": password
        })
        pd.DataFrame(s).to_csv('out/用户信息表.csv')
        return jsonify(json.loads(_json(
            {
                "value": 1
            }
        )))


@app.route('/<age>/div201')
def div201(age):
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    s = ""
    for c in list(data['疾病名称'].unique()):
        s += c * counts(list(data[data['疾病名称'] == c]['疾病名称']))
    _wei = weights(s)
    _key = keys(s)
    s = []
    for i in range(len(_wei)):
        s.append({
            "name": _key[i],
            "value": _wei[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/div202')
def div202y():
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    s = []
    for i in range(2015, 2022):
        s.append({
            "name": str(i),
            "value": counts(
                list(
                    data[data['年'] == int(i)]['年']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/div202')
def div202m(year):
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    s = []
    for i in range(1, 13):
        s.append({
            "name": str(i),
            "value": counts(
                list(
                    data[data['月'] == int(i)]['月']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/div202')
def div202d(year, month):
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    s = []
    data = data.sort_values(by=['日'])
    ri = list(data['日'].unique())
    for i in ri:
        s.append({
            "name": str(i),
            "value": counts(
                list(
                    data[data['日'] == int(i)]['日']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/div203')
def div203():
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    s = []
    for i in range(50, 120):
        s.append({
            "name": str(i),
            "value": counts(
                list(
                    data[data['年龄'] == int(i)]['年龄']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<xsq>/div204')
def div204(xsq):
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['县市区'] == xsq]
    s = []
    for i in list(data['疾病名称'].unique()):
        s.append({
            "name": str(i),
            "value": counts(
                list(
                    data[data['疾病名称'] == i]['疾病名称']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<zbmc>/l1')
def l1(zbmc):
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['疾病名称'] == zbmc]
    经度 = list(data['经度'].unique())
    纬度 = list(data['纬度'].unique())
    县市区 = list(data['县市区'].unique())
    s = []
    for i in range(len(经度)):
        s.append({
            "name": 县市区[i],
            "jd": 经度[i],
            "wd": 纬度[i],
            "value": counts(list(data[data['经度'] == 经度[i]]['经度']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<xsq>/<zbmc>/div205')
def div205(xsq, zbmc):
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['疾病名称'] == zbmc]
    data = data[data['县市区'] == xsq]
    idS = list(data['人员id'].unique())
    s = []
    for c in idS:
        s.append({
            "name": c,
            "value": counts(
                list(
                    data[data['人员id'] == c]['人员id']
                )
            )
        })
    data = pd.DataFrame(s)
    s = []
    for c in list(data['value'].unique()):
        s.append({
            "name": str(c) + "次",
            "value": counts(
                list(
                    data[data['value'] == int(c)]['value']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<year>/<month>/<day>/div206')
def div206(year, month, day):
    data = pd.read_csv('result/门诊病信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年'] == int(year)]
    data = data[data['月'] == int(month)]
    data = data[data['日'] == int(day)]
    s = ""
    for c in list(data['疾病名称'].unique()):
        s += c * counts(list(data[data['疾病名称'] == c]['疾病名称']))
    _wei = weights(s)
    _key = keys(s)
    s = []
    for i in range(len(_wei)):
        s.append({
            "name": _key[i],
            "value": _wei[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/l21')
def l21(age):
    data = pd.read_csv('result/签约信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    s = []
    经度 = list(data['经度'].unique())
    纬度 = list(data['纬度'].unique())
    医疗机构名称 = list(data['医疗机构名称'].unique())
    for i in range(len(经度)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "name": 医疗机构名称[i],
            "value": counts(
                list(
                    data[data['经度'] == 经度[i]]['经度']
                )
            ),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/l22')
def l22(age):
    data = pd.read_csv('result/长期参保信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    s = []
    经度 = list(data['经度'].unique())
    纬度 = list(data['纬度'].unique())
    护理机构名称 = list(data['护理机构名称'].unique())
    for i in range(len(经度)):
        s.append({
            "jd": 经度[i],
            "wd": 纬度[i],
            "name": 护理机构名称[i],
            "value": counts(
                list(
                    data[data['经度'] == 经度[i]]['经度']
                )
            ),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/div301')
def div301(age):
    data = pd.read_csv('result/签约信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    s = []
    for c in list(data['服务包名称'].unique()):
        s.append({
            "name": c,
            "value": counts(
                list(
                    data[data['服务包名称'] == c]['服务包名称']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/<jg1>/div302')
def div302(age, jg1):
    data = pd.read_csv('result/签约信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    data = data[data['医疗机构名称'] == jg1]
    s = []
    地址类型 = list(data['地址类型'])
    行政区划名称 = list(data['行政区划名称'])
    服务包名称 = list(data['服务包名称'])
    性别 = list(data['性别'])
    年龄 = list(data['年龄'])
    人员id = list(data['人员id'])

    for i in range(len(人员id)):
        s.append({
            "人员id": 人员id[i],
            "id": 人员id[i],
            "年龄": 年龄[i],
            "性别": 性别[i],
            "服务包名称": 服务包名称[i],
            "行政区划名称": 行政区划名称[i],
            "地址类型": 地址类型[i],
        })
    s = {
        "data": s,
        "describe": "",
        "fields": {
            "columns": [
                "年龄",
                "性别",
                "服务包名称",
                "行政区划名称",
                "地址类型",
                "id"
            ],
            "rows": [
                "人员id",
            ],
            "values": [],
        },
        "meta": [
            {
                "field": '地址类型',
                "name": '地址类型',
            },
            {
                "field": 'id',
                "name": 'id',
            },
            {
                "field": '年龄',
                "name": '年龄',
            },
            {
                "field": '性别',
                "name": '性别',
            },
            {
                "field": '服务包名称',
                "name": '服务包名称',
            },
            {
                "field": '行政区划名称',
                "name": '行政区划名称',
            },
            {
                "field": '地址类型',
                "name": '地址类型',
            },
        ]
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/<jg1>/div3021')
def div3021(age, jg1):
    data = pd.read_csv('result/签约信息.csv')
    data = data.dropna(axis=0, how='any')
    allPeopleNum = counts(list(data['年龄']))
    _data = data[data['年龄'] == int(age)]
    agePeopleNum = counts(list(_data['年龄']))
    _data = data[data['医疗机构名称'] == jg1]
    jg1PeopleNum = counts(list(_data['年龄']))
    data = data[data['年龄'] == int(age)]
    data = data[data['医疗机构名称'] == jg1]
    s = []
    for i in ['男', '女']:
        s.append({
            "name": i,
            "value": counts(list(data[data['性别'] == i]['性别']))
        })
    s = {
        "age": {
            "name": age,
            "value": agePeopleNum / allPeopleNum
        },
        "jg": {
            "name": jg1,
            "value": jg1PeopleNum / allPeopleNum
        },
        "data": s
    }
    return jsonify(json.loads(_json(s)))


@app.route('/div303')
def div303():
    data = pd.read_csv('result/签约信息.csv')
    data = data.dropna(axis=0, how='any')
    s = []
    for i in range(60, 110):
        for j in ['男', '女']:
            _data = data[data['年龄'] == int(i)]
            _data = _data[_data['性别'] == j]
            s.append({
                "name": str(i) + "岁",
                "type": j,
                "value": counts(
                    list(
                        _data['性别']
                    )
                )
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/div304')
def div304(age):
    data = pd.read_csv('result/长期参保信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    s = []
    for c in list(data['护理机构名称'].unique()):
        s.append({
            "name": c,
            "value": counts(
                list(
                    data[data['护理机构名称'] == c]['护理机构名称']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/<jg>/div305')
def div305(age, jg):
    data = pd.read_csv('result/长期参保信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    data = data[data['护理机构名称'] == jg]
    s = []
    地址类型 = list(data['地址类型'])
    出生年月 = list(data['出生年月'])
    城市 = list(data['城市'])
    人员ID = list(data['人员ID'])
    年龄 = list(data['年龄'])
    for i in range(len(人员ID)):
        s.append({
            "人员id": 人员ID[i],
            "id": 人员ID[i],
            "年龄": 年龄[i],
            "地址类型": 地址类型[i],
            "出生年月": 出生年月[i],
            "城市": 城市[i]
        })
    s = {
        "data": s,
        "describe": "",
        "fields": {
            "columns": [
                "年龄",
                "出生年月",
                "城市",
                "地址类型",
                "id"
            ],
            "rows": [
                "人员id",
            ],
            "values": [],
        },
        "meta": [
            {
                "field": '地址类型',
                "name": '地址类型',
            },
            {
                "field": 'id',
                "name": 'id',
            },
            {
                "field": '年龄',
                "name": '年龄',
            },
            {
                "field": '出生年月',
                "name": '出生年月',
            },
            {
                "field": '城市',
                "name": '城市',
            },
            {
                "field": '地址类型',
                "name": '地址类型',
            },
        ]
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<age>/div3051')
def div3051(age):
    data = pd.read_csv('result/长期参保信息.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(age)]
    s = []
    for i in list(data['城市'].unique()):
        s.append({
            "name": i,
            "value": counts(
                list(
                    data[data['城市'] == i]['城市']
                )
            )
        })
    return jsonify(json.loads(_json(s)))


@app.route('/div306')
def div306():
    data = pd.read_csv('result/长期参保信息.csv')
    data = data.dropna(axis=0, how='any')
    s = []
    for i in range(30, 100):
        for j in list(data['地址类型'].unique()):
            _data = data[data['年龄'] == int(i)]
            _data = _data[_data['地址类型'] == j]
            s.append({
                "name": str(i) + "岁",
                "type": j,
                "value": counts(
                    list(
                        _data['城市']
                    )
                )
            })
    return jsonify(json.loads(_json(s)))


@app.route('/div401')
def div401():
    data = pd.read_csv('result/主要年份人口情况.csv')
    s = []
    for c in list(data['年份'].unique()):
        _data = data[data['年份'] == int(c)]
        s.append({
            "name": str(c),
            "type": "常住人口",
            "value": avr(list(_data['常住人口']))
        })
        s.append({
            "name": str(c),
            "type": "城镇人口",
            "value": avr(list(_data['城镇人口']))
        })
        s.append({
            "name": str(c),
            "type": "市区人口",
            "value": avr(list(_data['市区人口']))
        })
        s.append({
            "name": str(c),
            "type": "城镇化率",
            "value": avr(list(_data['城镇化率']))
        })
        s.append({
            "name": str(c),
            "type": "户籍人口",
            "value": avr(list(_data['户籍人口']))
        })
        s.append({
            "name": str(c),
            "type": "市区人口",
            "value": avr(list(_data['市区人口']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<types>/div402')
def div402(types):
    data = pd.read_csv('result/六次普查_' + str(types) + ".csv")
    s = []
    headers = list(data.head(0))[1:]
    for i in list(data['普查时间'].unique()):
        _data = data[data['普查时间'] == i]
        for header in headers:
            s.append({
                "name": i,
                "type": header,
                "value": avr(list(_data[header]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/div403')
def div403():
    data = pd.read_csv('result/出生死亡增长率.csv')
    s = []
    headers = list(data.head(0))[1:]
    for i in list(data['地区'].unique()):
        _data = data[data['地区'] == i]
        for header in headers:
            s.append({
                "name": i,
                "type": header,
                "value": avr(list(_data[header]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/div404')
def div404():
    data = pd.read_csv('result/年末户籍人口数.csv')
    s = []
    headers = list(data.head(0))[1:]
    for i in list(data['地区'].unique()):
        _data = data[data['地区'] == i]
        for header in headers:
            s.append({
                "name": i,
                "type": header,
                "value": avr(list(_data[header]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/div405')
def div405():
    data = pd.read_csv('result/户籍人口基本情况.csv')
    s = []
    headers = list(data.head(0))[1:]
    for i in list(data['年份'].unique()):
        _data = data[data['年份'] == i]
        for header in headers:
            s.append({
                "name": i,
                "type": header,
                "value": avr(list(_data[header]))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/div406')
def div406(x):
    data = pd.read_csv('result/年鉴建模数据/七次人口普查数据.csv')
    data = data.dropna(axis=0, how='any')
    时间 = list(data['时间'])
    name = x
    x = list(data[x])
    s = []
    for i in range(len(x)):
        s.append({
            "name": str(时间[i]),
            name: float(x[i]),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/div407')
def div407(x):
    data = pd.read_csv('result/年鉴建模数据/主要年份人口情况.csv')
    data = data.dropna(axis=0, how='any')
    时间 = list(data['年份'])
    name = x
    x = list(data[x])
    s = []
    for i in range(len(x)):
        s.append({
            "name": str(时间[i]),
            name: float(x[i]),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/div408')
def div408(x):
    data = pd.read_csv('result/年鉴建模数据/农村住户人均食品消费量.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['食品类别'] == x]
    data = data.sort_values(by=['时间'])
    时间 = list(data['时间'])
    x = list(data['食品消耗量'])
    s = []
    for i in range(len(x)):
        s.append({
            "name": str(时间[i]),
            '食品消耗量': float(x[i]),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/div409')
def div409(x):
    data = pd.read_csv('result/年鉴建模数据/卫生机构情况.csv')
    data = data.dropna(axis=0, how='any')
    时间 = list(data['时间'])
    name = x
    x = list(data[x])
    s = []
    for i in range(len(x)):
        s.append({
            "name": str(时间[i]),
            name: float(x[i]),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/div410')
def div410(x, y):
    data = pd.read_csv('result/年鉴建模数据/各地区人口数据.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['地区'] == x]
    data = data.sort_values(by=['时间'])
    时间 = list(data['时间'])
    name = y
    y = list(data[y])
    s = []
    for i in range(len(y)):
        s.append({
            "name": str(时间[i]),
            name: float(y[i]),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/div411')
def div411(x):
    data = pd.read_csv('result/年鉴建模数据/各地区生产总值.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['地区'] == x]
    data = data.sort_values(by=['时间'])
    时间 = list(data['时间'])
    x = list(data['生产总值'])
    s = []
    for i in range(len(x)):
        s.append({
            "name": str(时间[i]),
            '生产总值': float(x[i]),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/div412')
def div412(x):
    data = pd.read_csv('result/年鉴建模数据/建筑业生产总值.csv')
    data = data.dropna(axis=0, how='any')
    时间 = list(data['时间'])
    x = list(data[x])
    s = []
    for i in range(len(x)):
        s.append({
            "name": str(时间[i]),
            "生产总值": float(x[i]),
        })
    return jsonify(json.loads(_json(s)))


@app.route('/div413')
def div413():
    data = pd.read_csv('result/65岁以上老年人人数.csv')
    年份 = list(data['年份'])
    人数 = list(data['人数'])
    s = []
    for i in range(len(人数)):
        s.append({
            "name": 年份[i],
            "value": 人数[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<code>/<password>/checkUser2')
def checkUser2(code, password):
    data = pd.read_csv('out/机构信息表.csv')
    data = data[data['code'] == code]
    if str(password) == str(list(data['password'])[0]):
        return jsonify(json.loads(_json(
            {
                "value": 1
            }
        )))
    else:
        return jsonify(json.loads(_json(
            {
                "value": 0
            }
        )))


@app.route('/<code>/<password>/regisUser2')
def regisUser2(code, password):
    data = pd.read_csv('out/机构信息表.csv')
    data = data[data['code'] == code]
    if len(list(data['code'])):
        return jsonify(json.loads(_json(
            {
                "value": 0
            }
        )))
    else:
        data = pd.read_csv('out/机构信息表.csv')
        s = []
        codes = list(data['code'])
        passwords = list(data['password'])
        for i in range(len(codes)):
            s.append({
                "code": codes[i],
                "password": passwords[i]
            })
        s.append({
            "code": code,
            "password": password
        })
        pd.DataFrame(s).to_csv('out/机构信息表.csv')
        return jsonify(json.loads(_json(
            {
                "value": 1
            }
        )))


app.run(
    host='127.0.0.1',
    port=5000,
    debug=True
)
