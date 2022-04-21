import jieba
import os
import pandas as pd


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


def toCsv(dicts, url):
    pd.DataFrame(dicts).to_csv(url, index=0)


mkdir('data')

data = pd.read_csv('data.csv')

岗位类型 = list(data['岗位类型'].unique())
岗位名称 = list(data['岗位名称'].unique())
薪资 = list(data['薪资'].unique())
城市 = list(data['城市'].unique())
工作经验 = list(data['工作经验'].unique())
学历 = list(data['学历'].unique())
工作类型 = list(data['工作类型'].unique())
公司名称 = list(data['公司名称'].unique())


def div1():
    """
    某一属性(岗位类型、工作类型)的柱状图(div1)
    """
    s = []
    for i in 岗位类型:
        _data = data[data['岗位类型'] == i]
        s.append({
            "name": i,
            "value": len(list(_data['岗位类型']))
        })
    pd.DataFrame(s).to_csv("data/岗位类型div1.csv", index=0)
    s = []
    for i in 工作类型:
        _data = data[data['工作类型'] == i]
        s.append({
            "name": i,
            "value": len(list(_data['工作类型']))
        })
    pd.DataFrame(s).to_csv("data/工作类型div1.csv", index=0)
    print("div1")


def div2():
    """
    属性一(学历、工作经验)与属性二(城市、工作类型)的平均薪资热力图(div2)
    """
    s = []
    for i in 学历:
        for j in 城市:
            _data = data[data['学历'] == i]
            _data = _data[_data['城市'] == j]
            s.append({
                "name1": i,
                "name2": j,
                "value": avr(list(_data['平均薪资']))
            })
    toCsv(s, "data/学历城市div2.csv")
    s = []
    for i in 学历:
        for j in 工作类型:
            _data = data[data['学历'] == i]
            _data = _data[_data['工作类型'] == j]
            s.append({
                "name1": i,
                "name2": j,
                "value": avr(list(_data['平均薪资']))
            })
    toCsv(s, "data/学历工作类型div2.csv")
    s = []
    for i in 工作经验:
        for j in 城市:
            _data = data[data['工作经验'] == i]
            _data = _data[_data['城市'] == j]
            s.append({
                "name1": i,
                "name2": j,
                "value": avr(list(_data['平均薪资']))
            })
    toCsv(s, "data/工作经验城市div2.csv")
    s = []
    for i in 工作经验:
        for j in 工作类型:
            _data = data[data['工作经验'] == i]
            _data = _data[_data['工作类型'] == j]
            s.append({
                "name1": i,
                "name2": j,
                "value": avr(list(_data['平均薪资']))
            })
    toCsv(s, "data/工作经验工作类型div2.csv")
    print("div2")


def div3():
    """
    岗位类型在学历(工作经验、城市)下的平均薪资条形图(div3)
    """
    s = []
    for i in 岗位类型:
        for j in 学历:
            _data = data[data['岗位类型'] == i]
            _data = _data[_data['学历'] == j]
            s.append({
                "name1": i,
                "name2": j,
                "value": avr(list(_data['平均薪资']))
            })
    toCsv(s, "data/岗位类型学历div3.csv")
    s = []
    for i in 岗位类型:
        for j in 工作经验:
            _data = data[data['岗位类型'] == i]
            _data = _data[_data['工作经验'] == j]
            s.append({
                "name1": i,
                "name2": j,
                "value": avr(list(_data['平均薪资']))
            })
    toCsv(s, "data/岗位类型工作经验div3.csv")
    s = []
    for i in 岗位类型:
        for j in 城市:
            _data = data[data['岗位类型'] == i]
            _data = _data[_data['城市'] == j]
            s.append({
                "name1": i,
                "name2": j,
                "value": avr(list(_data['平均薪资']))
            })
    toCsv(s, "data/岗位类型城市div3.csv")
    print("div3")


def div5():
    """
    选中的岗位类型的技能需求(岗位描述)词云图（div5）
    """
    for i in 岗位类型:
        _data = data[data['岗位类型'] == i]
        L = list(_data['岗位描述'].unique())
        _s = ""
        for c in L[: 100]:
            _s += str(c)
        _k = keys(_s, 30)
        _v = weights(_s, 30)
        s = []
        for j in range(len(_k)):
            s.append({
                "name": _k[j],
                "value": _v[j]
            })
        toCsv(s, "data/" + str(i) + "岗位描述div5.csv")
        _data = data[data['岗位类型'] == i]
        L = list(_data['技能需求'].unique())
        _s = ""
        for c in L[: 100]:
            _s += str(c)
        _k = keys(_s, 30)
        _v = weights(_s, 30)
        s = []
        for j in range(len(_k)):
            s.append({
                "name": _k[j],
                "value": _v[j]
            })
        toCsv(s, "data/" + str(i) + "技能需求div5.csv")
        print("♦️", end="")
    print("div5")


def m1():
    for i in 岗位类型:
        _data = data[data['岗位类型'] == i]
        经度 = list(_data['经度'].unique())
        纬度 = list(_data['纬度'].unique())
        s = []
        for j in range(len(经度)):
            s.append({
                "lng": 经度[j],
                "lat": 纬度[j],
                "value": avr(list(_data[_data['经度'] == 经度[j]]['平均薪资']))
            })
        toCsv(s, "data/" + str(i) + "m1.csv")
    print("m1")


def m3():
    for i in 岗位类型:
        _data = data[data['岗位类型'] == i]
        经度 = list(_data['经度'].unique())
        纬度 = list(_data['纬度'].unique())
        s = []
        for j in range(len(经度)):
            s.append({
                "lng": 经度[j],
                "lat": 纬度[j],
                "value": counts(list(_data[_data['经度'] == 经度[j]]['平均薪资']))
            })
        toCsv(s, "data/" + str(i) + "m3.csv")
    print("m3")


data.loc[:, "技能需求"] = data["技能需求"].str.replace("'", "")
data.loc[:, "技能需求"] = data["技能需求"].str.replace('"', "")
data.loc[:, "岗位描述"] = data["岗位描述"].str.replace("'", "")
data.loc[:, "岗位描述"] = data["岗位描述"].str.replace('"', "")
data.loc[:, "公司名称"] = data["公司名称"].str.replace('"', "")
data.loc[:, "公司名称"] = data["公司名称"].str.replace(',', "")
data.to_csv('data.csv', index=0)
