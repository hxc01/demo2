import os
import math
import json
import jieba
import random
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
import os
import math
import json
import time
import jieba
import random
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import urllib.request
import urllib.error
import execjs
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import numpy
import csv
# 全局取消证书验证
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# 通过url获取数据
def get_page(url):
    # requests.get 自带 json.load
    page = requests.get(url)
    page = page.content
    # 将bytes转换成字符串
    page = page.decode('utf-8')
    return page


def get_json():
    """
     xiaolanzao, 2022.02.27
    【作用】
     读取本地文件，获取json信息
    【参数】
     无
    【返回】
     json字符串
    """
    # 读取本地文件
    f = open("疫情数据.txt", "r", encoding="utf-8")
    f_content = f.read()
    f.close()

    # json字符串前后关键词
    json_start = "try { window.getAreaStat = "
    # 字符串包含的括号要进行转义
    json_end = "}catch\(e\){}"

    # json字符串正则匹配
    # (.*?)是匹配所有内容
    regular_key = json_start + "(.*?)" + json_end
    # 参数rs.S可以无视换行符，将所有文本视作一个整体进行匹配
    re_content = re.search(regular_key, f_content, re.S)
    # group()用于获取正则匹配后的字符串
    content = re_content.group()

    # 去除json字符串的前后关键词
    content = content.replace(json_start, '')
    # 尾巴要去掉转义符号
    json_end = "}catch(e){}"
    content = content.replace(json_end, '')
    return content


def dxy_data_down(article_url):
    url = urlopen(article_url)
    soup = BeautifulSoup(url, 'html.parser')  # parser解析
    f = open("疫情数据.txt", "w", encoding="utf-8")
    f.write(str(soup))
    f.close()


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


def yiqing():
    dxy_data_down("https://ncov.dxy.cn/ncovh5/view/pneumonia")
    # json字符串前后关键词
    json_start = "try { window.getAreaStat = "
    # 字符串包含的括号要进行转义
    json_end = "}catch\(e\){}"
    # json字符串正则匹配
    # (.*?)是匹配所有内容
    regular_key = json_start + "(.*?)" + json_end
    json_content = get_json()

    def display_provinces(json_content, province_name):
        json_data = json.loads(json_content)
        for i in json_data:
            if i["provinceName"] == province_name:
                # 读取里面的城市信息
                try:
                    return i['statisticsData']
                except:
                    return "没有信息啊！！！"

    mkdir('data/疫情数据')
    # 爬取山东整体疫情发展
    data = pd.DataFrame(json.loads(get_page(display_provinces(json_content, "山东省")))['data'])
    data.to_csv('data/疫情数据/allYQ.csv', index=0)
    # 爬取山东各市区疫情发展情况
    priUrl = 'https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode='
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]

    # 破解反爬
    def get_content2(url, headers):
        '''
        @获取403禁止访问的网页
        '''
        randdom_header = random.choice(headers)

        req = urllib.request.Request(url)
        req.add_header("User-Agent", randdom_header)
        req.add_header("Host", "blog.csdn.net")
        req.add_header("Referer", "http://blog.csdn.net/")
        req.add_header("GET", url)
        content = urllib.request.urlopen(req).read()
        return content

    # 获取城市名和行政区划
    data = pd.read_csv('data/cityCode.csv')
    city = list(data['城市'])
    codes = list(data['行政区划代码'])
    for i in range(len(city)):
        data = pd.DataFrame(json.loads(
            get_content2(
                priUrl + str(codes[i]),
                my_headers
            )
        )['data']['list'])
        s = []
        dates = list(data['date'])
        todays = list(data['today'])
        totals = list(data['total'])
        for ii in range(len(dates)):
            _s = {}

            def appd(header, value):
                try:
                    _s.update({
                        header: int(value),
                    })
                except:
                    _s.update({
                        header: 0,
                    })

            _s.update({
                "日期": dates[ii]
            })
            appd("确诊", todays[ii]['confirm'])
            appd("疑似", todays[ii]['suspect'])
            appd("治愈", todays[ii]['heal'])
            appd("死亡", todays[ii]['dead'])
            appd("累计确诊", totals[ii]['confirm'])
            appd("累计疑似", totals[ii]['suspect'])
            appd("累计治愈", totals[ii]['heal'])
            appd("累计死亡", totals[ii]['dead'])
            s.append(_s)
        pd.DataFrame(s).to_csv(
            'data/疫情数据/' + city[i] + ".csv",
            index=0
        )
        print(city[i], "爬取成功")


def jiechu(date):
    s = []
    citys = list(pd.read_csv('data/cityCode.csv')['城市'])
    for id1 in range(5):
        city1 = citys[int(random.random() * 100) % len(citys)]
        for id2 in range(6, 50):
            city2 = citys[int(random.random() * 100) % len(citys)]
            s.append({
                "人员ID": id1,
                "接触人员ID": id2,
                "状态": "阳性",
                "接触日期": date,
                "接触城市": city2,
                "人员城市": city1
            })
            for id3 in range(51, 300):
                city3 = citys[int(random.random() * 100) % len(citys)]
                s.append({
                    "人员ID": id2,
                    "接触人员ID": id3,
                    "状态": "阴性",
                    "接触日期": date,
                    "接触城市": city3,
                    "人员城市": city2
                })
    pd.DataFrame(s).to_csv('data/接触数据/密接人员信息' + date + '.csv', index=0)


"""for j in range(10, 32):
    jiechu("2022-03-" + ("0" + str(j))[-2:])
for j in range(1, 6):
    jiechu("2022-04-" + ("0" + str(j))[-2:])"""


@app.route('/<y>/<m>/<d>/d101')
def d101(y, m, d):
    data = pd.read_csv('data/cityCode.csv')
    citys = list(data['城市'])
    s = []
    for city in citys:
        if '市' in city:
            data = pd.read_csv('data/疫情数据/' + city + '.csv')
        else:
            data = pd.read_csv('data/疫情数据/' + city + '市.csv')
        data.loc[:, "年"] = data['日期'].str.replace("-", "").astype('int64') // 10000
        data.loc[:, "月"] = data['日期'].str.replace("-", "").astype('int64') // 100 % 100
        data.loc[:, "日"] = data['日期'].str.replace("-", "").astype('int64') % 100
        data = data[data['年'] == int(y)]
        data = data[data['月'] == int(m)]
        data = data[data['日'] == int(d)]
        value = avr(list(data['累计确诊'])) - avr(list(data['累计治愈'])) - avr(list(data['累计死亡']))
        L = [
            avr(list(data['确诊'])),
            avr(list(data['疑似'])),
            avr(list(data['治愈'])),
            avr(list(data['死亡'])),
            avr(list(data['累计确诊'])),
            avr(list(data['累计疑似'])),
            avr(list(data['累计治愈'])),
            avr(list(data['累计死亡']))
        ]
        data = pd.read_csv('data/城市经纬度.csv')
        city = str(city).replace("市", "")
        data = data[data['城市'] == city]
        s.append({
            "name": city,
            "date": str(y) + "-" + str(m) + "-" + str(d),
            "jd": avr(list(data['经度'])),
            "wd": avr(list(data['纬度'])),
            "确诊": L[0],
            "疑似": L[1],
            "治愈": L[2],
            "死亡": L[3],
            "累计确诊": L[4],
            "累计疑似": L[5],
            "累计治愈": L[6],
            "累计死亡": L[7],
            "value": value
        })
    return jsonify(json.loads(_json(s)))


@app.route('/d102')
def d102():
    data = pd.read_csv('data/疫情数据/allYQ.csv')
    s = []
    for i in list(data['dateId']):
        _data = data[data['dateId'] == int(i)]
        s.append({
            "date": str(i),
            "type": "累计确诊",
            "value": avr(list(_data['confirmedCount']))
        })
        s.append({
            "date": str(i),
            "type": "累计疑似",
            "value": avr(list(_data['suspectedCount']))
        })
        s.append({
            "date": str(i),
            "type": "累计治愈",
            "value": avr(list(_data['curedCount']))
        })
        s.append({
            "date": str(i),
            "type": "累计死亡",
            "value": avr(list(_data['deadCount']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<city>/<types>/d103')
def d103(y, city, types):
    if '市' in city:
        data = pd.read_csv('data/疫情数据/' + city + '.csv')
    else:
        data = pd.read_csv('data/疫情数据/' + city + '市.csv')
    data.loc[:, "年"] = data['日期'].str.replace("-", "").astype('int64') // 10000
    data.loc[:, "月"] = data['日期'].str.replace("-", "").astype('int64') // 100 % 100
    data.loc[:, "日"] = data['日期'].str.replace("-", "").astype('int64') % 100
    data = data[data['年'] == int(y)]
    s = []
    maxL = 0
    for i in list(data['月'].unique()):
        for j in range(1, 32):
            _data = data[data['月'] == int(i)]
            _data = _data[_data['日'] == int(j)]
            s.append({
                "月": str(i) + "月",
                "日": str(j) + "日",
                "value": avr(list(_data[types]))
            })
            maxL = max(maxL, avr(list(_data[types])))
    return jsonify(json.loads(_json({
        "max": maxL,
        "data": s
    })))


@app.route('/<y>/<city>/d104')
def d104(y, city):
    if '市' in city:
        data = pd.read_csv('data/疫情数据/' + city + '.csv')
    else:
        data = pd.read_csv('data/疫情数据/' + city + '市.csv')
    data.loc[:, "年"] = data['日期'].str.replace("-", "").astype('int64') // 10000
    data.loc[:, "月"] = data['日期'].str.replace("-", "").astype('int64') // 100 % 100
    data.loc[:, "日"] = data['日期'].str.replace("-", "").astype('int64') % 100
    data = data[data['年'] == int(y)]
    s = []
    for i in list(data['日期']):
        _data = data[data['日期'] == i]
        s.append({
            "date": i,
            "type": "新增确诊",
            "value": avr(list(_data['确诊']))
        })
        s.append({
            "date": i,
            "type": "新增疑似",
            "value": avr(list(_data['疑似']))
        })
        s.append({
            "date": i,
            "type": "新增治愈",
            "value": avr(list(_data['治愈']))
        })
        s.append({
            "date": i,
            "type": "新增死亡",
            "value": avr(list(_data['死亡']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d201')
def d201(date):
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    data = data[data['状态'] == '阳性']
    s = []
    for i in list(data['人员城市'].unique()):
        _data = data[data['人员城市'] == i]
        for j in list(_data['接触城市'].unique()):
            __data = _data[_data['接触城市'] == j]
            s.append({
                "source": i,
                "target": j,
                "value": counts(list(__data['接触日期']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d202')
def d202(date):
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    data = data[data['状态'] == '阴性']
    s = []
    for i in list(data['人员城市'].unique()):
        _data = data[data['人员城市'] == i]
        for j in list(_data['接触城市'].unique()):
            __data = _data[_data['接触城市'] == j]
            s.append({
                "source": i,
                "target": j,
                "value": counts(list(__data['接触日期']))
            })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d203')
def d203(date):
    citys = pd.read_csv('data/城市经纬度.csv')
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    data = data[data['状态'] == "阳性"]
    s = []
    for i in list(data['人员城市'].unique()):
        _data = data[data['人员城市'] == i]
        x = i
        city = citys[citys['城市'] == x.replace("市", "")]
        s.append({
            "jd": avr(list(city['经度'])),
            "wd": avr(list(city['纬度'])),
            "value": counts(list(_data['人员城市']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d204')
def d204(date):
    citys = pd.read_csv('data/城市经纬度.csv')
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    data = data[data['状态'] == "阳性"]
    s = []
    for i in list(data['接触城市'].unique()):
        _data = data[data['接触城市'] == i]
        x = i
        city = citys[citys['城市'] == x.replace("市", "")]
        s.append({
            "jd": avr(list(city['经度'])),
            "wd": avr(list(city['纬度'])),
            "value": counts(list(_data['接触日期']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d205')
def d205(date):
    citys = pd.read_csv('data/城市经纬度.csv')
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    data = data[data['状态'] == "阴性"]
    s = []
    for i in list(data['接触城市'].unique()):
        _data = data[data['接触城市'] == i]
        x = i
        city = citys[citys['城市'] == x.replace("市", "")]
        s.append({
            "jd": avr(list(city['经度'])),
            "wd": avr(list(city['纬度'])),
            "value": counts(list(_data['接触日期']))
        })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d206')
def d206(date):
    citys = pd.read_csv('data/城市经纬度.csv')
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    s = []
    data1 = data[data['状态'] == '阳性']
    for i in list(data['人员城市'].unique()):
        for j in list(data['接触城市'].unique()):
            _data = data1[data1['人员城市'] == i]
            _data = _data[_data['接触城市'] == j]
            x = i
            y = j
            city1 = citys[citys['城市'] == x.replace("市", "")]
            city2 = citys[citys['城市'] == y.replace("市", "")]
            if len(list(city1['经度'])) and len(list(city2['经度'])):
                s.append({
                    "jd1": avr(list(city1['经度'])),
                    "wd1": avr(list(city1['纬度'])),
                    "jd2": avr(list(city2['经度'])),
                    "wd2": avr(list(city2['纬度'])),
                    "type": "密接",
                    "value": counts(list(_data['接触日期']))
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/d207')
def d207(date):
    citys = pd.read_csv('data/城市经纬度.csv')
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    s = []
    data1 = data[data['状态'] == '阴性']
    for i in list(data['人员城市'].unique()):
        for j in list(data['接触城市'].unique()):
            _data = data1[data1['人员城市'] == i]
            _data = _data[_data['接触城市'] == j]
            x = i
            y = j
            city1 = citys[citys['城市'] == x.replace("市", "")]
            city2 = citys[citys['城市'] == y.replace("市", "")]
            if len(list(city1['经度'])) and len(list(city2['经度'])):
                s.append({
                    "jd1": avr(list(city1['经度'])),
                    "wd1": avr(list(city1['纬度'])),
                    "jd2": avr(list(city2['经度'])),
                    "wd2": avr(list(city2['纬度'])),
                    "type": "密接",
                    "value": counts(list(_data['接触日期']))
                })
    return jsonify(json.loads(_json(s)))


@app.route('/<y>/<m>/<d>/d301')
def d301(y, m, d):
    data = pd.read_csv('data/cityCode.csv')
    citys = list(data['城市'])
    if '市' in citys[0]:
        data = pd.read_csv('data/疫情数据/' + citys[0] + '.csv')
    else:
        data = pd.read_csv('data/疫情数据/' + citys[0] + '市.csv')
    s = []
    L = []
    columns = [{
        "prop": "城市",
        "label": "城市",
        "width": "150"
    }]
    headers = list(data.head(0))
    for header in headers:
        L.append(list(data[header]))
    for header in headers:
        columns.append({
            "prop": header,
            "label": header,
            "width": "150"
        })
    for city in citys:
        if '市' in city:
            data = pd.read_csv('data/疫情数据/' + city + '.csv')
        else:
            data = pd.read_csv('data/疫情数据/' + city + '市.csv')
        data.loc[:, "年"] = data['日期'].str.replace("-", "").astype('int64') // 10000
        data.loc[:, "月"] = data['日期'].str.replace("-", "").astype('int64') // 100 % 100
        data.loc[:, "日"] = data['日期'].str.replace("-", "").astype('int64') % 100
        data = data[data['年'] == int(y)]
        data = data[data['月'] == int(m)]
        data = data[data['日'] == int(d)]
        try:
            _s = {}
            for j in range(len(L)):
                _s.update({
                    headers[j]: list(data[headers[j]])[0]
                })
            _s.update({
                "城市": city
            })
            s.append(_s)
        except:
            a = 1
    s = {
        "data": s,
        "columns": columns
    }
    return jsonify(json.loads(_json(s)))


@app.route('/<date>/<city1>/<city2>/d401')
def d401(date, city1, city2):
    data = pd.read_csv('data/接触数据/密接人员信息' + date + '.csv')
    data = data[data['人员城市'] == city1]
    data = data[data['接触城市'] == city2]
    headers = list(data.head(0))
    s = []
    L = []
    for header in headers:
        L.append(list(data[header]))
    for i in range(len(L[0])):
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


app.run(host='127.0.0.1', port=4500, debug=True)
