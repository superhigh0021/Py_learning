# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import operator
 
"""
函数说明:创建数据样本
Returns:
    dataset - 实验样本切分的词条
    classVec - 类别标签向量
""" 
def loadDataSet():
    dataset = [['my', 'my', 'dog', 'has', 'flea', 'problems', 'help', 'stupid'],  # 切分的词条8
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],# 8
               ['my', 'dalmation', 'is', 'so', 'cute', 'problems', 'love', 'him'],  # 8
               ['i','stop', 'posting', 'stupid', 'worthless', 'garbage', 'study'],   # 7
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop'],  # 8
               ['quit', 'buying', 'worthless', 'dog', 'food', 'sun', 'sun']]  # 7
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表好，0代表不好
    return dataset, classVec
 
 
"""
函数说明：特征选择TF-IDF算法
Parameters: list_words:词列表
Returns: dict_feature_select:特征选择词字典
""" 
def feature_select(list_words):
    # 总词频统计
    doc_frequency = defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i] += 1
    print('doc_frequency: '  ,len(doc_frequency)  ,doc_frequency)
    # 计算每个词的TF值
    word_tf = {}  # 存储没个词的tf值
    for i in doc_frequency:
        word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())
    print('每个单词在总数出现的频率word_tf ： ',len(word_tf),word_tf)
    # 计算每个词的IDF值
    doc_num = len(list_words)  #  6
    word_idf = {}  # 存储每个词的idf值
    word_doc = defaultdict(int)  # 存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i] += 1
    for i in doc_frequency:
        word_idf[i] = math.log(doc_num / (word_doc[i] + 1))
    print('每个单词在总数出现的频率 word_idf ：',len(word_idf),word_idf)
    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for i in doc_frequency:
        word_tf_idf[i] = word_tf[i] * word_idf[i]
    print('word_tf_idf=word_tf[i]* word_idf[i]',len(word_tf_idf),word_tf_idf)
    # 对字典按值由大到小排序
    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    print('对字典按值由大到小排序dict_feature' ,dict_feature_select)
    return dict_feature_select
 
 
if __name__ == '__main__':
    data_list, label_list = loadDataSet()  # 加载数据
    print(data_list,'\n',label_list)
    features = feature_select(data_list)  # 所有词的TF-IDF值
    print(features)
    print(len(features))