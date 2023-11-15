import pandas as pd
import numpy as np
# 读取文件
path = './KualaLumpur.csv'
data = pd.read_csv(path)
new_path = './KualaLumpur_new.csv'
new_data = pd.read_csv(new_path)
#第一次处理
def change_nei(data,path,k):
    df1 = pd.read_csv(path, encoding='UTF-8',usecols=[k])#选取第1，5，7列
    df2 = df1.drop_duplicates(subset=None, keep='first', inplace=False)
    #subset是根据字段去除重复，多个字段就写成列表形式，默认是所有列
    #keep first就是保留第一个，last就是最后
    #inplace 默认为False，不直接进行修改
    #print(df2)
    #查找这一行的所有重复元素
    NEIGHBORHOOD_list = []
    column_list = df2.iloc[:, 0].tolist()
    for item in column_list:
        NEIGHBORHOOD_list.append(item)
    #print(NEIGHBORHOOD_list)
    new_NEIGHBORHOOD_list=[]
    for i in range(len(NEIGHBORHOOD_list)):
        new_NEIGHBORHOOD_list.append(i)
    #print(new_NEIGHBORHOOD_list)
    data.replace(NEIGHBORHOOD_list, new_NEIGHBORHOOD_list, inplace=True)
    #data.drop(columns=data.columns[0], axis=1, inplace=True)
    data.to_csv(new_path,index=False)
#后面的处理
def street(data,path,k):
    df1 = pd.read_csv(path, encoding='UTF-8', usecols=[k])  # 选取第1，5，7列
    df2 = df1.drop_duplicates(subset=None, keep='first', inplace=False)
    # subset是根据字段去除重复，多个字段就写成列表形式，默认是所有列
    # keep first就是保留第一个，last就是最后
    # inplace 默认为False，不直接进行修改
    #print(df2)
    # 查找这一行的所有重复元素
    NEIGHBORHOOD_list = []
    #获取这一列的元素存在一个列表里
    column_list = df2.iloc[:, 0].tolist()
    for item in column_list:
        NEIGHBORHOOD_list.append(item)
    #print(NEIGHBORHOOD_list)
    new_NEIGHBORHOOD_list = []
    for i in range(len(NEIGHBORHOOD_list)):
        new_NEIGHBORHOOD_list.append(i)
    #print(new_NEIGHBORHOOD_list)
    data.replace(NEIGHBORHOOD_list, new_NEIGHBORHOOD_list, inplace=True)
    data.to_csv(new_path, index=False)
#



#main

#change_nei(data,path,0)
def two():
    new_data = pd.read_csv(new_path)
    street(new_data,new_path,7)
two()
