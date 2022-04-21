import pandas as pd
import math


def sums(li):
    s = 0
    for c in li:
        s += c
    return s


def ln(x):
    return math.log(x, 2.718281828459)


def toDict(dicts, name, value):
    ss = []
    for ii in dicts:
        ss.append({
            name: ii,
            value: dicts[ii]
        })
    return ss


def toDict2(dicts, name, types, value):
    ss = []
    for ii in dicts:
        for jj in dicts[ii]:
            ss.append({
                name: ii,
                types: jj,
                value: dicts[ii][jj]
            })
    return ss


def toDict3(dicts, name, type1, type2, value):
    ss = []
    for ii in dicts:
        for jj in dicts[ii]:
            for kk in dicts[ii][jj]:
                ss.append({
                    name: ii,
                    type1: jj,
                    type2: kk,
                    value: dicts[ii][jj][kk]
                })
    return ss


def toCsv(dicts, url):
    pd.DataFrame(dicts).to_csv(url, index=0)


"""
数据导入
"""
人口数据 = pd.read_csv('data/人口数据.csv')
电力数据 = pd.read_csv('data/电力数据.csv')
能源数据 = pd.read_csv('data/能源数据.csv')
地区经济数据 = pd.read_csv('data/地区经济数据.csv')
行业经济数据 = pd.read_csv('data/行业经济数据.csv')
能源CO2排放系数 = pd.read_csv('out/能源CO2排放系数.csv')

"""
数据处理，
通过（行业）连接【电力数据】和【行业经济数据】，行数 498 -> 243
通过（能源类别）连接【能源数据】和【能源CO2排放系数】，行数 37 -> 33
"""
电力数据 = pd.merge(电力数据, 行业经济数据, on=['行业', '年份'])
电力数据.to_csv('result/电力数据.csv', index=0)
电力数据 = pd.read_csv('result/电力数据.csv')
能源数据 = pd.merge(能源数据, 能源CO2排放系数, on=['能源类别'])
能源数据.to_csv('result/能源数据.csv', index=0)
能源数据 = pd.read_csv('result/能源数据.csv')
"""
将下标保存
"""
y = list(电力数据['年份'].unique())
c = list(电力数据['产业'].unique())
e = list(能源数据['能源类别'].unique())

"""
建模
"""
global C, C1  # C：碳排放总量、C1：不同产业的不同能源排放的碳
global N1  # N1：CO2排放系数
global P1  # P1：不同产业能源消耗占比
global E1, E2, E3  # E1：产业类别同年电力消耗、E2：不同产业不同能源的消耗、E3：不同能源总消耗、E4：总电力消耗
global M1, M2  # M1：不同产业经济增加值、M2：GDP
global A, A1  # A：总人口、A1：城镇人口
# D1：能源结构、D2：能源强度、D3：能源消费效率、D4：产业结构 D5：经济发展、D6：城镇化水平、D7：人口规模
global D1, D2, D3, D4, D5, D6, D7
# I1：能源结构、I2：能源强度、I3：能源消费效率、I4：产业结构 I5：经济发展、I6：城镇化水平、I7：人口规模
global I1, I2, I3, I4, I5, I6, I7

"""
部分全局变量赋值
"""
N1 = {}
for i in range(len(e)):
    N1.update({
        e[i]: list(能源数据[能源数据['能源类别'] == e[i]]['CO2排放系数'])[0]
    })
# print("N1CO2排放系数：", N1)

"""
碳排放总量模型
"""
C = {}
for i in range(len(y)):
    E3 = {}
    _data = 能源数据[能源数据['年份'] == int(y[i])]
    if len(_data['能源类别']) > 0:
        ll = []
        for j in range(len(e)):
            try:
                E3.update({
                    e[j]: list(_data[_data['能源类别'] == e[j]]['能耗消耗'])[0]
                })
                # E3 * N1
                ll.append(E3[e[j]] * N1[e[j]])
            except:
                a = 1
        if len(ll) > 0:
            C.update({
                # sum(E3, N1){E3 * N1}
                y[i]: sums(ll)
            })
# print("C碳排放总量模型完成：", C)

"""
常量预备
"""

# 计算P1, E2
P1 = {}
E2 = {}
C1 = {}
for i in range(len(y)):
    E1 = {}
    E4 = 0
    _data = 电力数据[电力数据['年份'] == int(y[i])]
    for j in range(len(c)):
        ll = sums(list(_data[_data['产业'] == c[j]]['用电量（千瓦时）']))
        E1.update({
            c[j]: ll
        })
        # E4 += ll

    data = pd.read_csv('data/能源数据.csv')
    data = data[data['能源类别'] == '电力消费量(亿千瓦小时)']
    data = data[data['年份'] == int(y[i])]
    try:
        E4 = list(data['能耗消耗'])[0] * 1e8
    except:
        break

    l1 = {}
    for j in range(len(c)):
        l1.update({
            # P1 = E1 / E4
            c[j]: E1[c[j]] / E4
        })
    P1.update({
        y[i]: l1
    })

    E3 = {}
    ll1 = {}
    _data = 能源数据[能源数据['年份'] == int(y[i])]
    if len(_data['能源类别']) > 0:
        ll = []
        for j in range(len(e)):
            ll2 = {}
            try:
                E3.update({
                    e[j]: list(_data[_data['能源类别'] == e[j]]['能耗消耗'])[0]
                })
                ll.append(E3[e[j]] * N1[e[j]])
            except:
                a = 1
            for k in range(len(c)):
                ll2.update({
                    # E2 = P1 * E3
                    c[k]: round(E3[e[j]] * l1[c[k]], 4)
                })
            ll1.update({
                e[j]: ll2
            })
        E2.update({
            y[i]: ll1
        })
    E3 = {}
    ll1 = {}
    _data = 能源数据[能源数据['年份'] == int(y[i])]
    if len(_data['能源类别']) > 0:
        ll = []
        for j in range(len(e)):
            ll2 = {}
            try:
                E3.update({
                    e[j]: list(_data[_data['能源类别'] == e[j]]['能耗消耗'])[0]
                })
                ll.append(E3[e[j]] * N1[e[j]])
            except:
                a = 1
            for k in range(len(c)):
                ll2.update({
                    # C1 = E2 * N1
                    c[k]: round(E3[e[j]] * l1[c[k]], 4) * N1[e[j]]
                })
            ll1.update({
                e[j]: ll2
            })
        C1.update({
            y[i]: ll1
        })
# print("P1模型完成：", P1)
# print("E2模型完成：", E2)
# print("C1模型完成：", C1)

"""
因素分解
"""

# 计算E3
E3 = {}
for i in range(len(y)):
    _data = 能源数据[能源数据['年份'] == int(y[i])]
    if len(_data['能源类别']) > 0:
        ll = {}
        for j in range(len(e)):
            try:
                ll.update({
                    e[j]: list(_data[_data['能源类别'] == e[j]]['能耗消耗'])[0]
                })
            except:
                a = 1
        if len(ll) > 0:
            E3.update({
                y[i]: ll
            })
# print("E3不同能源总消耗：", E3)

# 读取M1, M2, A1, A
M1 = {}
M2 = {}
A1 = {}
A = {}
for i in y:
    _data = 行业经济数据[行业经济数据['年份'] == int(i)]
    l1 = {}
    for j in c:
        __data = _data[_data['产业'] == j]
        l2 = list(__data['经济增加值（亿元）'])
        l1.update({
            j: sums(l2)
        })
    M1.update({
        i: l1
    })

    _data = 地区经济数据[地区经济数据['年份'] == int(i)]
    M2.update({
        i: list(_data['GDP（亿元）'])[0]
    })

    _data = 人口数据
    _data = _data[_data['年份'] == int(i)]
    A.update({
        i: list(_data[_data['城镇类别'] == '城镇人口']['人口（万人）'])[0] + list(_data[_data['城镇类别'] == '农村人口']['人口（万人）'])[0]
    })
    _data = 人口数据[人口数据['城镇类别'] == '城镇人口']
    A1.update({
        i: list(_data[_data['城镇类别'] == '城镇人口']['人口（万人）'])[0]
    })

# print("M1不同产业经济增加值：", M1)
# print("M2GDP：", M2)
# print("A1城镇人口：", A1)
# print("A总人口：", A)

"""
计算D1, D2
"""
D1 = {}
D2 = {}
D3 = {}
D4 = {}
D5 = {}
D6 = {}
D7 = {}
for i in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]:
    l1 = {}
    for j in e:
        l2 = {}
        for k in c:
            try:
                l2.update({
                    # D1 = E2 / (P1 * E3)
                    k: E2[i][j][k] / (P1[i][k] * E3[i][j])
                })
            except:
                break
        l1.update({
            j: l2
        })
    D1.update({
        i: l1
    })

    l1 = {}
    for j in e:
        l2 = {}
        for k in c:
            try:
                l2.update({
                    # D2 = C1 * E2
                    k: E2[i][j][k] / C1[i][j][k]
                })
            except:
                break
        l1.update({
            j: l2
        })
    D2.update({
        i: l1
    })

    l1 = {}
    for k in e:
        l2 = {}
        for j in c:
            try:
                l2.update({
                    # D3 = (P1 * E3) / M1
                    j: round(P1[i][j] * E3[i][k] / M1[i][j], 6)
                })
            except:
                a = 1
        l1.update({
            k: l2
        })
    D3.update({
        i: l1
    })

    l1 = {}
    for j in c:
        l1.update({
            # D4 = M1 / M2
            j: M1[i][j] / M2[i]
        })
    D4.update({
        i: l1
    })

    D5.update({
        # D5 = M2 / A1
        i: M2[i] / A1[i]
    })

    D6.update({
        # D6 = A1 / A
        i: A1[i] / A[i]
    })

    D7.update({
        # D7 = A
        i: A[i]
    })

# print("D1模型完成：", D1)
# print("D2模型完成：", D2)
# print("D3模型完成：", D3)
# print("D4模型完成：", D4)
# print("D5模型完成：", D5)
# print("D6模型完成：", D6)
# print("D7模型完成：", D7)

"""
计算I1 ～ I7
"""
I1 = {}
I2 = {}
I3 = {}
I4 = {}
I5 = {}
I6 = {}
I7 = {}
y = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

for i in range(len(y) - 1):
    lastY = int(y[i])
    nowY = int(y[i + 1])

    s = 0
    for j in e:
        for k in c:
            try:
                _a = ln(D1[nowY][j][k] / D1[lastY][j][k])
                _b = C1[nowY][j][k] - C1[lastY][j][k]
                _c = ln(C1[nowY][j][k]) - ln(C1[lastY][j][k])
                s += _a * _b / _c
            except:
                s += 0
    I1.update({
        str(lastY) + str(nowY): s
    })

    s = 0
    for j in e:
        for k in c:
            try:
                _a = ln(D2[nowY][j][k] / D2[lastY][j][k])
                _b = C1[nowY][j][k] - C1[lastY][j][k]
                _c = ln(C1[nowY][j][k]) - ln(C1[lastY][j][k])
                s += _a * _b / _c
            except:
                s += 0
    I2.update({
        str(lastY) + str(nowY): s
    })

    s = 0
    for j in e:
        for k in c:
            try:
                _a = ln(D3[nowY][j][k] / D3[lastY][j][k])
                _b = C1[nowY][j][k] - C1[lastY][j][k]
                _c = ln(C1[nowY][j][k]) - ln(C1[lastY][j][k])
                s += _a * _b / _c
            except:
                s += 0
    I3.update({
        str(lastY) + str(nowY): s
    })

    s = 0
    for j in e:
        for k in c:
            try:
                _a = ln(D4[nowY][k] / D4[lastY][k])
                _b = C1[nowY][j][k] - C1[lastY][j][k]
                _c = ln(C1[nowY][j][k]) - ln(C1[lastY][j][k])
                s += _a * _b / _c
            except:
                s += 0
    I4.update({
        str(lastY) + str(nowY): s
    })

    s = 0
    for j in e:
        for k in c:
            try:
                _a = ln(D5[nowY] / D5[lastY])
                _b = C1[nowY][j][k] - C1[lastY][j][k]
                _c = ln(C1[nowY][j][k]) - ln(C1[lastY][j][k])
                s += _a * _b / _c
            except:
                s += 0
    I5.update({
        str(lastY) + str(nowY): s
    })

    s = 0
    for j in e:
        for k in c:
            try:
                _a = ln(D6[nowY] / D6[lastY])
                _b = C1[nowY][j][k] - C1[lastY][j][k]
                _c = ln(C1[nowY][j][k]) - ln(C1[lastY][j][k])
                s += _a * _b / _c
            except:
                s += 0
    I6.update({
        str(lastY) + str(nowY): s
    })

    s = 0
    for j in e:
        for k in c:
            try:
                _a = ln(D7[nowY] / D7[lastY])
                _b = C1[nowY][j][k] - C1[lastY][j][k]
                _c = ln(C1[nowY][j][k]) - ln(C1[lastY][j][k])
                s += _a * _b / _c
            except:
                s += 0
    I7.update({
        str(lastY) + str(nowY): s
    })

# print("I1: ", I1)
# print("I2: ", I2)
# print("I3: ", I3)
# print("I4: ", I4)
# print("I5: ", I5)
# print("I6: ", I6)
# print("I7: ", I7)

D = [D1, D2, D3, D4, D5, D6, D7]
I = [I1, I2, I3, I4, I5, I6, I7]

toCsv(toDict3(D1, "年份", "能源类别", "产业类别", 'value'), 'moxing/能源结构(因素).csv')
toCsv(toDict3(D2, "年份", "能源类别", "产业类别", 'value'), 'moxing/能源强度(因素).csv')
toCsv(toDict3(D3, "年份", "能源类别", "产业类别", 'value'), 'moxing/能源消费效率(因素).csv')
toCsv(toDict2(D4, "年份", "产业", 'value'), 'moxing/产业结构(因素).csv')
toCsv(toDict(D5, "年份", 'value'), 'moxing/经济发展(因素).csv')
toCsv(toDict(D6, "年份", 'value'), 'moxing/城镇化水平(因素).csv')
toCsv(toDict(D7, "年份", 'value'), 'moxing/人口规模(因素).csv')

toCsv(toDict(I1, "年份", 'value'), 'moxing/能源结构(因素效应).csv')
toCsv(toDict(I2, "年份", 'value'), 'moxing/能源强度(因素效应).csv')
toCsv(toDict(I3, "年份", 'value'), 'moxing/能源消费效率(因素效应).csv')
toCsv(toDict(I4, "年份", 'value'), 'moxing/产业结构(因素效应).csv')
toCsv(toDict(I5, "年份", 'value'), 'moxing/经济发展(因素效应).csv')
toCsv(toDict(I6, "年份", 'value'), 'moxing/城镇化水平(因素效应).csv')
toCsv(toDict(I7, "年份", 'value'), 'moxing/人口规模(因素效应).csv')



