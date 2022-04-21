import os
import math
import json
import jieba
import random
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import date


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


@app.route('/<xx>/<yy>/d1')
def d1(xx, yy):
    data = pd.read_csv('data/医保数据.csv', usecols=['年龄', '诊断名称', '性别', '入院日期', '出院日期'])
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(xx)]
    data = data[data['诊断名称'] == yy]
    data = data[data['性别'] == '男']
    s = []
    出院日期 = list(data['入院日期'])
    入院日期 = list(data['出院日期'])
    for i in range(len(入院日期)):
        x = 出院日期[i].split("/")
        y = 入院日期[i].split("/")
        date1 = date(int(x[0]), int(x[1]), int(x[2]))
        date2 = date(int(y[0]), int(y[1]), int(y[2]))
        v = 1
        if "days" in str(date2 - date1):
            v = int(str(date2 - date1).split(" ")[0])
        s.append({
            "value": v
        })
    boyTime = avr(list(pd.DataFrame(s)['value']))
    data = pd.read_csv('data/医保数据.csv')
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(xx)]
    data = data[data['诊断名称'] == yy]
    data = data[data['性别'] == '女']
    s = []
    出院日期 = list(data['入院日期'])
    入院日期 = list(data['出院日期'])
    for i in range(len(入院日期)):
        x = 出院日期[i].split("/", 2)
        y = 入院日期[i].split("/", 2)
        date1 = date(int(x[0]), int(x[1]), int(x[2]))
        date2 = date(int(y[0]), int(y[1]), int(y[2]))
        v = 1
        if "days" in str(date2 - date1):
            v = int(str(date2 - date1).split(" ")[0])
        s.append({
            "value": v
        })
    girlTime = avr(list(pd.DataFrame(s)['value']))
    s = [{
        "name": "男",
        "平均住院时长": boyTime
    }, {
        "name": "女",
        "平均住院时长": girlTime
    }]
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d2')
def d2(x):
    data = pd.read_csv('data/医保数据.csv', usecols=['年龄', '诊断名称'])
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(x)]
    s = []
    for i in list(data['诊断名称'].unique()):
        _data = data[data['诊断名称'] == i]
        s.append({
            "诊断名称": i,
            "诊断人数": counts(list(_data['诊断名称']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d3')
def d3(x):
    data = pd.read_csv('data/医保数据.csv', usecols=['年龄', '总费用', '统筹费用'])
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(x)]
    s = []
    总费用 = list(data['总费用'])
    统筹费用 = list(data['统筹费用'])
    for i in range(len(总费用)):
        if 总费用[i] != 0:
            s.append({
                "value": float(统筹费用[i]) / float(总费用[i])
            })
    s = {
        "value": avr(
            list(
                pd.DataFrame(s)['value']
            )
        )
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d4')
def d4(x):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '总费用', '统筹费用'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    s = []
    总费用 = list(data['总费用'])
    统筹费用 = list(data['统筹费用'])
    for i in range(len(总费用)):
        try:
            s.append({
                "value": float(统筹费用[i]) / float(总费用[i])
            })
        except:
            a = 1
    s = {
        "value": avr(
            list(
                pd.DataFrame(s)['value']
            )
        )
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d5')
def d5(x):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '年龄'])
    data = data.dropna(axis=0, how='any')
    data = data[data['年龄'] == int(x)]
    s = ""
    for c in list(data['诊断名称']):
        s += str(c)
    _k = keys(s)
    _w = weights(s)
    s = []
    for i in range(len(_k)):
        s.append({
            "name": _k[i],
            "value": _w[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d6')
def d6(x):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '年龄', '性别'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    s = []
    for i in range(0, 120):
        for j in ['男', '女']:
            _data = data[data['年龄'] == int(i)]
            _data = _data[_data['性别'] == j]
            s.append({
                "年龄": str(i),
                "性别": j,
                "人数": counts(list(_data['年龄']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<ZDMC>/d7')
def d7(ZDMC):
    data = pd.read_csv('json/' + str(ZDMC) + "div5.csv")
    JGDJ = list(data['JGDJ'])
    percent = list(data['percent'])
    s = []
    for i in range(len(JGDJ)):
        s.append({
            "JGDJ": JGDJ[i],
            "percent": percent[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<ZDMC>/d8')
def d8(ZDMC):
    data = pd.read_csv('json/' + str(ZDMC) + "div6.csv")
    JGDJ = list(data['JGDJ'])
    percent = list(data['percent'])
    s = []
    for i in range(len(JGDJ)):
        s.append({
            "JGDJ": JGDJ[i],
            "percent": percent[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d9')
def d9(x, y):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '性别', '年龄', '机构等级', '统筹费用'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    data = data[data['机构等级'] == y]
    s = []
    for j in ['男', '女']:
        for i in range(0, 120):
            _data = data[data['性别'] == j]
            _data = _data[_data['年龄'] == int(i)]
            if counts(list(_data['年龄'])):
                s.append({
                    "年龄": str(i),
                    "性别": j,
                    "平均统筹费用": avr(list(_data['统筹费用']))
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d10')
def d10(x):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '机构等级'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    s = []
    for i in ['一级', '二级', '三级']:
        _data = data[data['机构等级'] == i]
        s.append({
            "机构等级": i,
            "就诊人数": counts(list(_data['机构等级']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d12')
def d12(x, y):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '机构等级', '人员城市'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    data = data[data['机构等级'] == y]
    s = []
    for i in list(data['人员城市'].unique()):
        _data = data[data['人员城市'] == i]
        s.append({
            "人员城市": i,
            "就诊人数": counts(list(_data['人员城市']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d13')
def d13(x):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '医疗类别'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    s = []
    for i in list(data['医疗类别'].unique()):
        _data = data[data['医疗类别'] == i]
        s.append({
            "医疗类别": i,
            "就诊人数": counts(list(_data['医疗类别']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d11')
def d11(x, y):
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '性别', '医疗类别'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    data = data[data['医疗类别'] == y]
    s = []
    for i in ['男', '女']:
        _data = data[data['性别'] == i]
        s.append({
            "性别": i,
            "就诊人数": counts(list(_data['医疗类别']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/heat')
def heat(x):
    s = []
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '就诊经度', '就诊纬度', '就诊城市'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    就诊经度 = list(data['就诊经度'].unique())
    就诊纬度 = list(data['就诊纬度'].unique())
    就诊城市 = list(data['就诊城市'].unique())
    for i in range(len(就诊纬度)):
        _data = data[data['就诊城市'] == 就诊城市[i]]
        s.append({
            "jd": 就诊经度[i],
            "wd": 就诊纬度[i],
            "就诊城市": 就诊城市[i],
            "value": counts(list(_data['就诊城市']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<NL>/<XB>/flyLines')
def flyLines(x, NL, XB):
    s = []
    data = pd.read_csv('data/医保数据.csv', usecols=['诊断名称', '年龄', '性别', '人员城市', '人员经度', '人员纬度', '就诊城市', '就诊经度', '就诊纬度'])
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    data = data[data['年龄'] == int(NL)]
    data = data[data['性别'] == XB]
    人员城市 = list(data['人员城市'])
    人员经度 = list(data['人员经度'])
    人员纬度 = list(data['人员纬度'])
    就诊城市 = list(data['就诊城市'])
    就诊经度 = list(data['就诊经度'])
    就诊纬度 = list(data['就诊纬度'])
    for i in range(len(人员城市)):
        if 就诊经度[i] != 人员经度[i] and 就诊纬度[i] != 人员纬度[i]:
            s.append({
                "就诊城市": 就诊城市[i],
                "lng2": 就诊经度[i],
                "lat2": 就诊纬度[i],
                "人员城市": 人员城市[i],
                "lng1": 人员经度[i],
                "lat1": 人员纬度[i]
            })
    return jsonify(json.loads(_json(s)))


@app.route('/d201')
def d201():
    data = pd.read_csv('data/脱贫享受政策医疗总费用保障表.csv')
    s = []
    L1 = list(data['治疗人次'])
    L2 = list(data['自付'])
    行政区划 = list(data['行政区划'])
    for i in range(len(L1)):
        s.append({
            "name": 行政区划[i],
            "value": 1 - round(L2[i] / (L1[i] * 10000), 3)
        })
    return jsonify(json.loads(_json(s)))


@app.route('/d202')
def d202():
    data = pd.read_csv('data/脱贫享受政策医疗总费用保障表.csv')
    s = []
    headers = ['住院部分', '门诊部分', '购药部分', '基本医保', '大病保险', '医疗救助', '商业补充保险', '政府兜底', '慈善基金', '临时救助', '扶贫基金', '医院减免', '其他',
               '自付', '人均自付']
    for header in headers:
        L = list(data[header])
        行政区划 = list(data['行政区划'])
        for i in range(len(L)):
            s.append({
                "行政区划": 行政区划[i],
                "type": header,
                "value": L[i]
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d203')
def d203(x):
    data = pd.read_csv('data/脱贫享受政策医疗总费用保障表.csv')
    data = data[data['行政区划'] == x]
    s = []
    headers = ['住院部分', '门诊部分', '购药部分', '基本医保', '大病保险', '医疗救助', '商业补充保险', '政府兜底', '慈善基金', '临时救助', '扶贫基金', '医院减免', '其他',
               '自付', '人均自付']
    for header in headers:
        L = list(data[header])
        s.append({
            "name": header,
            "value": avr(L)
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d204')
def d204(x):
    data = pd.read_csv('data/脱贫享受政策医疗总费用保障表.csv')
    s = []
    L = list(data[x])
    行政区划 = list(data['行政区划'])
    for i in range(len(L)):
        s.append({
            "name": 行政区划[i],
            "value": L[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/d205')
def d205():
    data = pd.read_csv('data/脱贫享受政策医疗总费用保障表.csv')
    s = []
    L1 = list(data['治疗人次'])
    L2 = list(data['总费用'])
    行政区划 = list(data['行政区划'])
    for i in range(len(L1)):
        s.append({
            "name": 行政区划[i],
            "治疗人次": L1[i],
            "总费用": L2[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/l201')
def l201(x):
    data = pd.read_csv('data/脱贫享受政策医疗总费用保障表.csv')
    s = []
    L = list(data[x])
    行政区划 = list(data['行政区划'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    for i in range(len(L)):
        s.append({
            "name": 行政区划[i],
            "value": L[i],
            "jd": 经度[i],
            'wd': 纬度[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/l301')
def l301():
    data = pd.read_csv('data/日照市市管民营医疗机构信息.csv')
    data = data.dropna(axis=0, how='any')
    机构地址 = list(data['机构地址'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    机构等次 = list(data['机构等次'])
    经营性质 = list(data['经营性质'])
    机构级别 = list(data['机构级别'])
    联系电话 = list(data['联系电话'])
    机构名称 = list(data['机构名称'])
    s = []
    for i in range(len(经度)):
        s.append({
            "机构地址": 机构地址[i],
            "经度": 经度[i],
            "纬度": 纬度[i],
            "机构等次": 机构等次[i],
            "经营性质": 经营性质[i],
            "机构级别": 机构级别[i],
            "联系电话": 联系电话[i],
            "机构名称": 机构名称[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/l302')
def l302():
    data = pd.read_csv('data/日照市基层医疗卫生机构信息（乡镇卫生院）.csv')
    s = []
    机构地址 = list(data['机构地址'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    机构名称 = list(data['机构名称'])
    联系电话 = list(data['联系电话'])
    for i in range(len(经度)):
        s.append({
            "机构地址": 机构地址[i],
            "经度": 经度[i],
            "纬度": 纬度[i],
            "机构名称": 机构名称[i],
            "联系电话": 联系电话[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/l303')
def l303():
    data = pd.read_csv('data/日照市基层医疗卫生机构信息（社区卫生服务中心）.csv')
    s = []
    机构地址 = list(data['机构地址'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    联系电话 = list(data['联系电话'])
    机构名称 = list(data['机构名称'])
    for i in range(len(经度)):
        s.append({
            "机构地址": 机构地址[i],
            "经度": 经度[i],
            "纬度": 纬度[i],
            "联系电话": 联系电话[i],
            "机构名称": 机构名称[i],
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/l304')
def l304(x):
    data = pd.read_csv('data/日照市各县区GDP.csv')
    县区 = list(data['县区'])
    经度 = list(data['经度'])
    纬度 = list(data['纬度'])
    L = list(data[x])
    s = []
    for i in range(len(L)):
        s.append({
            "县区": 县区[i],
            "经度": 经度[i],
            "纬度": 纬度[i],
            "value": L[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/d301')
def d301():
    data = pd.read_csv(
        'data/日照市公立医疗机构病种价格.csv',
        usecols=['手术名称', '二级医疗机构价格', '疾病名称', '三级医疗机构价格'],
        encoding="gbk"
    )
    data = data.dropna(axis=0, how='any')
    手术名称 = list(data['手术名称'])
    二级医疗机构价格 = list(data['二级医疗机构价格'])
    疾病名称 = list(data['疾病名称'])
    三级医疗机构价格 = list(data['三级医疗机构价格'])
    s = []
    for i in range(len(手术名称)):
        s.append({
            "手术名称": 手术名称[i],
            "疾病名称": 疾病名称[i],
            "type": "二级医疗机构",
            "value": 二级医疗机构价格[i]
        })
        s.append({
            "手术名称": 手术名称[i],
            "疾病名称": 疾病名称[i],
            "type": "三级医疗机构",
            "value": 三级医疗机构价格[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d302')
def d302(x, y):
    data = pd.read_csv('data/日照市各县区GDP.csv')
    L1 = list(data[x])
    L2 = list(data[y])
    name = list(data['县区'])
    s = []
    for i in range(len(name)):
        s.append({
            "县区": name[i],
            x: L1[i],
            y: L2[i]
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d303_4')
def d303_4(x):
    data = pd.read_csv('data/日照市各县区GDP.csv')
    GDPMax = maxs(list(data['GDP']))
    常住人口Max = maxs(list(data['常住人口']))
    户籍人口Max = maxs(list(data['户籍人口']))
    面积Max = maxs(list(data['面积']))
    s = []
    data = data[data['县区'] == x]
    GDP = avr(list(data['GDP']))
    常住人口 = avr(list(data['常住人口']))
    户籍人口 = avr(list(data['户籍人口']))
    面积 = avr(list(data['面积']))
    s.append({
        "name": "GDP",
        "value": round(GDP / GDPMax, 3)
    })
    s.append({
        "name": "常住人口",
        "value": round(常住人口 / 常住人口Max, 3)
    })
    s.append({
        "name": "户籍人口",
        "value": round(户籍人口 / 户籍人口Max, 3)
    })
    s.append({
        "name": "面积",
        "value": round(面积 / 面积Max, 3)
    })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d305')
def d305(x):
    data = pd.read_csv('data/日照市各县区GDP.csv')
    s = []
    GDP = list(data['GDP'])
    常住人口 = list(data['常住人口'])
    户籍人口 = list(data['户籍人口'])
    面积 = list(data['面积'])
    人均面积 = []
    人均GDP = []
    常住占比 = []
    for i in range(len(面积)):
        人均面积.append(面积[i] / 常住人口[i])
        人均GDP.append(GDP[i] / 常住人口[i])
        常住占比.append(常住人口[i] / 户籍人口[i])
    人均面积Max = maxs(人均面积)
    人均GDPMax = maxs(人均GDP)
    常住占比Max = maxs(常住占比)
    data = data[data['县区'] == x]
    GDP = avr(list(data['GDP']))
    常住人口 = avr(list(data['常住人口']))
    户籍人口 = avr(list(data['户籍人口']))
    面积 = avr(list(data['面积']))
    人均面积 = 面积 / 常住人口
    人均GDP = GDP / 常住人口
    常住占比 = 常住人口 / 户籍人口
    s.append({
        "人均面积": round(人均面积 / 人均面积Max, 2),
        "人均GDP": round(人均GDP / 人均GDPMax, 2),
        "常住占比": round(常住占比 / 常住占比Max, 2)
    })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/<m>/<d>/l401_2')
def l401_2(x, y, m, d):
    data = pd.read_csv("data/医保数据.csv")
    data = data.dropna(axis=0, how='any')
    data = data[data['诊断名称'] == x]
    data = data[data['入院年'] == int(y)]
    data = data[data['入院月'] == int(m)]
    data = data[data['入院日'] == int(d)]
    街道经度 = list(data['街道经度'].unique())
    街道纬度 = list(data['街道纬度'].unique())
    街道名称 = list(data['街道名称'].unique())
    s = []
    for i in range(len(街道经度)):
        _data = data[data['街道名称'] == i]
        s.append({
            "街道名称": 街道名称[i],
            "jd": 街道经度[i],
            "wd": 街道纬度[i],
            "value": counts(list(_data['街道名称']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d401')
def d401(x):
    data = pd.read_csv("data/医保数据.csv")
    data = data.dropna(axis=0, how='any')
    data = data[data['医疗类别'] == x]
    s = []
    for i in list(data['入院年'].unique()):
        _data = data[data['入院年'] == int(i)]
        _s = []
        for j in list(_data['入院月'].unique()):
            __s = []
            __data = _data[_data['入院月'] == int(j)]
            for k in range(1, 31):
                if counts(list(__data['入院日'])) != 0:
                    ___data = __data[__data['入院日'] == int(k)]
                    __s.append({
                        "name": str(k),
                        "value": counts(list(___data['入院日']))
                    })
            _s.append({
                "name": str(j),
                "value": counts(list(__data['入院日'])),
                "children": __s
            })
        s.append({
            "name": str(i),
            "value": counts(list(_data['入院日'])),
            "children": _s
        })
    s = s[0]
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/<z>/d402')
def d402(x, y, z):
    data = pd.read_csv("data/医保数据.csv")
    data = data.dropna(axis=0, how='any')
    data = data[data['入院年'] == int(x)]
    data = data[data['入院月'] == int(y)]
    data = data[data['入院日'] == int(z)]
    s = []
    for c in list(data['诊断名称'].unique()):
        _data = data[data['诊断名称'] == c]
        s.append({
            "name": c,
            "value": counts(list(_data['诊断名称']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d403')
def d403(x):
    data = pd.read_csv('data/医保数据.csv')
    data = data[data['诊断名称'] == x]
    s = []
    for i in list(data['街道名称'].unique()):
        _data = data[data['街道名称'] == i]
        s.append({
            "name": i,
            "value": counts(list(_data['街道名称']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/<z>/d404')
def d404(x, y, z):
    data = pd.read_csv("data/医保数据.csv")
    data = data.dropna(axis=0, how='any')
    data = data[data['入院年'] == int(x)]
    data = data[data['入院月'] == int(y)]
    data = data[data['入院日'] == int(z)]
    s = []
    for c in list(data['诊断名称'].unique()):
        _data = data[data['诊断名称'] == c]
        出院日期 = list(_data['出院日期'])
        入院日期 = list(_data['入院日期'])
        sum_l = 0
        for i in range(len(出院日期)):
            x = 入院日期[i].split("/")
            y = 出院日期[i].split("/")
            date1 = date(int(x[0]), int(x[1]), int(x[2]))
            date2 = date(int(y[0]), int(y[1]), int(y[2]))
            v = 1
            if "days" in str(date2 - date1):
                v = int(str(date2 - date1).split(" ")[0])
            sum_l += v
        s.append({
            "name": c,
            "value": round(sum_l / len(出院日期), 2)
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d5011')
def d5011(x):
    data = pd.read_csv('prival/医保大数据.csv')
    data = data[data['诊断名称'] == x]

    maxI = 0
    maxL = 0
    for i in list(data['性别'].unique()):
        if maxL < counts(list(data[data['性别'] == i])):
            maxI = i
    xb = maxI


    sss = []
    for i in list(data['年龄'].unique()):
        sss.append({
            "name": i,
            "value": counts(list(data[data['年龄'] == int(i)]))
        })
    sss = pd.DataFrame(sss).sort_values(by=['value'], ascending=False)
    sss = list(sss['name'])[:3]
    nl = [
        min(sss),
        max(sss)
    ]

    maxI = 0
    maxL = 0
    for i in list(data['机构等级'].unique()):
        if maxL < counts(list(data[data['机构等级'] == i])):
            maxI = i
    jgdj = maxI

    maxI = 0
    maxL = 0
    for i in list(data['医疗类别'].unique()):
        if maxL < counts(list(data[data['医疗类别'] == i])):
            maxI = i
    yllb = maxI

    maxI = 0
    maxL = 0
    for i in list(data['街道名称'].unique()):
        if maxL < counts(list(data[data['街道名称'] == i])):
            maxI = i
    jdmc = maxI

    maxY = 2017
    maxM = 1
    maxL = 0
    for i in list(data['入院年'].unique()):
        for j in list(data['入院月'].unique()):
            _data = data[data['入院年'] == int(i)]
            _data = _data[_data['入院月'] == int(j)]
            if maxL < counts(list(_data['入院月'])):
                maxY = i
                maxM = j
                maxL = counts(list(_data['入院月']))
    ryY = maxY
    ryM = maxM

    总费用 = list(data['总费用'])
    统筹费用 = list(data['统筹费用'])
    sumL = 0
    num = 0
    for i in range(len(总费用)):
        try:
            sumL += (统筹费用[i] / 总费用[i])
            num += 1
        except:
            sumL += 0
    tcbl = sumL / num

    s1 = "■ 在诊断数据中，" + str(xb) + "性居多;"
    s2 = "■ 易病人群的年龄集中在" + str(nl[0]) + "岁 ～" + str(nl[1]) + "岁"
    s3 = "■ 大部分病人都选择在" + str(jgdj) + "医院进行就诊"
    s4 = "■ 选择的救治方式，通常是" + str(yllb)
    s5 = "■ 从街道数据中，可以得出，大部分病人来自" + str(jdmc)
    s6 = "■ 在近几年中, 就诊时间都集中在" + str(ryM) + "月"
    s7 = "■ 该病症的平均报销比例是" + str(round(tcbl, 4)*10)[:5] + "%"
    return jsonify(json.loads(_json({
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "s4": s4,
        "s5": s5,
        "s6": s6,
        "s7": s7,
    })))


@app.route('/<y>/<x>/d5012')
def d5012(x, y):
    data = pd.read_csv('prival/医保大数据.csv')
    data = data[data['诊断名称'] == x]
    data = data[data['入院年'] == int(y)]
    s = []
    for i in range(1, 13):
        for j in list(data['性别'].unique()):
            _data = data[data['入院月'] == int(i)]
            _data = _data[_data['性别'] == j]
            s.append({
                "name": str(i) + "月",
                "type": j,
                "value": counts(list(_data['性别']))
            })
    return jsonify(json.loads(_json(s)))



@app.route('/<x>/d502')
def d502(x):
    data = pd.read_csv('data/医保数据.csv',
                       usecols=['年龄', '人员城市', '就诊城市', '诊断名称', '就诊纬度', '就诊经度', '人员纬度', '人员经度', '统筹费用']
                       )
    data = data[data['年龄'] == int(x)]
    jd = 119
    wd = 35
    nodes = []
    links = []
    categories = []
    for c in list(data['人员城市'].unique()):
        categories.append({
            "name": c
        })
    a = 0
    for i in list(data['就诊城市'].unique()):
        try:
            a += 1
            _data = data[data['就诊城市'] == i]
            nodes.append({
                "id": str(a),
                "name": i.replace(",", "").replace("，", "").replace("'", ""),
                "symbolSize": min(counts(list(_data['人员城市'])), 100) / 5,
                "x": (jd - avr(list(_data['人员经度'])) + random.random()) * 150,
                "y": (wd - avr(list(_data['人员纬度'])) + random.random()) * 100,
                "value": avr(list(_data['统筹费用'])),
                "category": list(data['人员城市'].unique()).index(list(_data['人员城市'])[0])
            })
            b = a
            for j in list(_data['诊断名称'].unique()):
                b += 1
                __data = _data[_data['诊断名称'] == j]
                nodes.append({
                    "id": str(b),
                    "name": j.replace(",", "").replace("，", "").replace("'", ""),
                    "symbolSize": min(counts(list(__data['人员城市'])), 100) / 5,
                    "x": (jd - avr(list(__data['就诊经度'])) + random.random()) * 150,
                    "y": (wd - avr(list(__data['就诊纬度'])) + random.random()) * 100,
                    "value": avr(list(__data['统筹费用'])),
                    "category": list(data['人员城市'].unique()).index(list(__data['就诊城市'])[0])
                })
                links.append({
                    "source": str(a),
                    "target": str(b)
                })
            a = b
        except:
            xxxx = 1
    s = {
        "nodes": nodes,
        "links": links,
        "categories": categories
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d503')
def d503(x, y):
    data = pd.read_csv('data/医保数据.csv',
                       usecols=['人员城市', '诊断名称', '年龄']
                       )
    data = data[data['人员城市'] == x]
    data = data[data['诊断名称'] == y]
    s = []
    for i in range(120):
        _data = data[data['年龄'] == int(i)]
        s.append({
            "name": i,
            "value": counts(_data['年龄'])
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/d504')
def d504(x):
    data = pd.read_csv('data/医保数据.csv',
                       usecols=['性别', '人员城市', '就诊城市', '诊断名称']
                       )
    data = data[data['诊断名称'] == x]
    s = []
    for i in list(data['性别'].unique()):
        data1 = data[data['性别'] == i]
        for j in list(data1['人员城市'].unique()):
            data2 = data1[data1['人员城市'] == j]
            s.append({
                "source": i,
                "target": j,
                "value": counts(list(data2['人员城市']))
            })
            for k in list(data2['就诊城市'].unique()):
                data3 = data2[data2['就诊城市'] == k]
                s.append({
                    "source": j,
                    "target": k,
                    "value": counts(list(data3['人员城市']))
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<a>/<b>/<c>/<d>/d601')
def d601(a, b, c, d):
    data = pd.read_csv('data/医保数据.csv')
    data = data[data['人员城市'] == a]
    data = data[data['就诊城市'] == b]
    data = data[data['医疗类别'] == c]
    data = data[data['机构等级'] == d]
    s = []
    headers = []
    sxHeaders = ['人员城市', '就诊城市', '医疗类别', '机构等级', 'ID', '就诊经度', '就诊纬度', '人员城市', '人员经度', '人员纬度', '街道经度', '街道纬度', '入院年',
                 '入院月', '入院日', '出院年', '出院月', '出院日']
    for header in list(data.head(0)):
        if header in sxHeaders:
            s = []
        else:
            headers.append(header)
    length = len(list(data[headers[0]]))
    for i in range(length):
        _s = {}
        for header in headers:
            _s.update({
                header: list(data[header])[i]
            })
        s.append(_s)
    columns = []
    for header in headers:
        columns.append({
            "prop": header,
            "label": header,
            "width": 200
        })
    s = {
        "data": s,
        "column": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/d602')
def d602():
    data = pd.read_csv('data/既往史样例数据.csv')
    s = []
    headers = []
    for header in list(data.head(0)):
        headers.append(header)
    length = len(list(data[headers[0]]))
    for i in range(length):
        _s = {}
        for header in headers:
            _s.update({
                header: list(data[header])[i]
            })
        s.append(_s)
    columns = []
    for header in headers:
        columns.append({
            "prop": header,
            "label": header,
            "width": 200
        })
    s = {
        "data": s,
        "column": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/d603')
def d603(x, y):
    data = pd.read_csv('prival/医保大数据.csv',
        usecols=['入院年', '入院月', '入院日', '诊断名称'])
    data = data[data['入院年'] == int(x)]
    data = data[data['诊断名称'] == y]
    s = []
    for i in range(1, 13):
        _data = data[data['入院月'] == int(i)]
        length = counts(list(_data['诊断名称']))
        for j in range(1, 32):
            __data = _data[_data['入院日'] == int(j)]
            try:
                s.append({
                    "month": str(i),
                    "day": str(j),
                    "value": counts(list(__data['诊断名称'])) / length * 10
                })
            except:
                s.append({
                    "month": str(i),
                    "day": str(j),
                    "value": 0
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<x>/<y>/<z>/d604')
def d604(x, y, z):
    data = pd.read_csv('prival/医保大数据.csv', usecols=['入院年', '入院月', '入院日', '诊断名称'])
    data = data[data['入院年'] == int(x)]
    data = data[data['入院月'] == int(y)]
    data = data[data['入院日'] == int(z)]
    s = []
    for i in list(data['诊断名称'].unique()):
        _data = data[data['诊断名称'] == i]
        s.append({
            "name": i,
            "value": counts(list(_data['诊断名称']))
        })
    return jsonify(json.loads(_json(s)))


app.run(
    host='127.0.0.1',
    port=1500
)













