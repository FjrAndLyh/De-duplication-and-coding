import pandas as pd
import numpy as np
# 读取文件
pd.options.display.max_rows=100000#解除输出限制
behind = '.csv'
#只需要修改datafile的名字就可以换成别的数据集
datafile = 'KualaLumpur'
path = './'+datafile +behind
save = './'+datafile+'/'
print(save)
data = pd.read_csv(path)

#邻居
def one(data,path,k):
    df1 = pd.read_csv(path, encoding='UTF-8',usecols=[k])#1相当于第二列
    df2 = df1.drop_duplicates(subset=None, keep='first', inplace=False)
    #subset是根据字段去除重复，多个字段就写成列表形式，默认是所有列
    #keep first就是保留第一个，last就是最后
    #inplace 默认为False，不直接进行修改
    #print(df2)
    #查找这一行的所有重复元素,存放在列表里
    NEIGHBORHOOD_list = []
    column_list = df2.iloc[:,0].tolist()
    #获取数据的标题
    title = list(df2)
    title0 = title[0]
    #将数据一一对应关系保存为csv并且取名为列名
    save_path = save + title0 + behind
    print(title[0])
    print(column_list)
    for item in column_list:
        NEIGHBORHOOD_list.append(item)
    print(NEIGHBORHOOD_list)
    #打印一一对应关系
    df2.insert(0, '对应值', range(len(df2)), allow_duplicates=False)
    print(df2)
    df2.to_csv(save_path)
    new_NEIGHBORHOOD_list=[]
    for i in range(len(NEIGHBORHOOD_list)):
        new_NEIGHBORHOOD_list.append(i)

    #替换重复数据

#街区


one(data,path,6)
