import pandas as pd

data1 = pd.read_csv('data/医保数据.csv', usecols=['人员区划', '人员城市', '人员经度', '人员纬度'])
print("3")
data2 = pd.read_csv('prival/医保数据.csv', usecols=['人员区划'])
print("5")
data = pd.merge(data1, data2, on=['人员区划'])
print("7")
data1 = pd.read_csv('data/医保数据.csv', usecols=['就诊区划', '就诊城市', '就诊经度', '就诊纬度'])
print("9")
data2 = pd.read_csv('prival/医保数据.csv', usecols=['就诊区划'])
print("11")
data.to_csv('prival/人员区划.csv', index=0)
print("13")
data = pd.merge(data1, data2, on=['就诊区划'])
print("15")
data.to_csv('prival/就诊区划.csv', index=0)
print("17")
