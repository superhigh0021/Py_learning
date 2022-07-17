#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Oct 30, 2017
朴素贝叶斯
'''
 
from numpy import * 
def loadDataSet():
    postingList = [['my', 'like', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him']]
                   #  ,
                   # ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]  # 每一行代表一篇文档
    classVec = [0, 1, 0, 1, 0]#, 1]  # 1代表侮辱性文字，0代表正常言论
    return postingList, classVec  # 返回数据集和类别标签
 
 
'''
使用set构造函数去除数据集中每篇文档的重复词语
''' 
def createVocabList(dataSet):
    vocabSet = set([])  # 创建一个空的集合
    for document in dataSet:  # 读取每一篇文档
        vocabSet = vocabSet | set(document)  # 两个集合的并操作
    return list(vocabSet)  # 返回不包含重复词语的列表，该列表包含所有词，并且以Ascll排序好
 
 
'''
在词汇表中，把一篇文档中出现的单词标记为1，其余标记为0
@param vocabList：词汇表
@param inputSet：一篇文档
''' 
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)  # 创建一个长度为len(vocabList)的零向量
    for word in inputSet:
        if word in vocabList:  # 如果该词汇出现在词汇表中，则找到该词汇在词汇表中的位置，标记为1
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)  # 提示后，忽略该不存在的词语
    return returnVec  # 返回一个和词汇表等长的0, 1向量
 
 
'''
朴素贝叶斯分类器训练函数
@param trainMatrix：文档矩阵，每一行为一个和词汇表等长的0, 1向量，行数代表文档个数
@param trainCategory：每篇文档的类别标签向量
'''  
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)  # 文档数目
    numWords = len(trainMatrix[0])  # 计算词汇表长度
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 计算属于侮辱性文档(class=1)的概率
    p0Num = ones(numWords);
    p1Num = ones(numWords)  # 分子，所有词出现数初始化为1，防止在计算P(w0|1)P(w1|1)P(w2|1)某个概率为0乘积就为0的情况发生
    p0Denom = 2.0;
    p1Denom = 2.0  # 分母，初始化次数为2，代表每一类文档至少有两个词，总词数
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:  # 如果该篇文档是侮辱性文档
            p1Num += trainMatrix[i]  # 每篇文档每个单词的次数累加
            p1Denom += sum(trainMatrix[i])  # 每篇文档总单词数累加
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)  # P(wi|c1)，词汇表中属于侮辱性词汇的每个单词在总单词中出现的概率，
    p0Vect = log(p0Num / p0Denom)  # P(wi|c0)，词汇表中属于非侮辱性词汇的每个单词的概率，用log防止多个小概率连乘后乘积变为0的情况
    print(p1Num,'\n', p1Denom,'\n',p1Vect)
    print(p0Num,'\n', p0Denom,'\n',p0Vect)
    return p0Vect, p1Vect, pAbusive  # 返回和词汇表等长的非侮辱性词汇的概率向量、和词汇表等长的侮辱性词汇的概率向量、侮辱性文档的概率
'''
print(p1Num,'\n', p1Denom,'\n',p1Vect)
打印结果：
[1. 1. 1. 1. 2. 1. 1. 1. 2. 1. 2. 2. 1. 1. 1. 2. 1. 2. 2. 1. 1. 2. 2. 1.1. 1. 1. 2. 3. 2.] 
 15.0   
 [-2.7080502  -2.7080502  -2.7080502  -2.7080502  -2.01490302 -2.7080502-2.7080502  -2.7080502  -2.01490302 -2.7080502  -2.01490302 -2.01490302
 -2.7080502  -2.7080502  -2.7080502  -2.01490302 -2.7080502  -2.01490302 -2.01490302 -2.7080502  -2.7080502  -2.01490302 -2.01490302 -2.7080502
 -2.7080502  -2.7080502  -2.7080502  -2.01490302 -1.60943791 -2.01490302]
'''
 
'''
朴素贝叶斯分类函数（对于一个待分类的文本，计算所有词汇概率之和属于哪一个类的概率最大，就确定为该类）
@param vec2Classify：待分类的和词汇表等长的0, 1向量
@param p0Vec：词汇表等长的非侮辱性词汇的概率向量
@param p1Vec：词汇表等长的侮辱性词汇的概率向量
@param pClass1：侮辱性词汇的文档概率 
则通过该函数计算得 p1 < p0 , vec2Classify 更可能划分为非侮辱性文档
'''
 
 
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # 对应元素相乘，然后相加，得到P(w|c1)，因为前面是log，故后面也是 +log
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)  # 对应元素相乘，然后相加，得到P(w|c0)，因为前面是log，故后面也是 +log
    if p1 > p0:
        return 1
    else:
        return 0
 
'''
使用朴素贝叶斯过滤网站的恶意留言
''' 
def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage', '33']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
 
 
testingNB()  # ['love', 'my', 'dalmation'] classified as:  0      ['stupid', 'garbage'] classified as:  1
 
'''
修改 setOfWords2Vec() 函数，变为词袋模型，每篇文档中的词汇可以出现多次
''' 
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec  # 返回一个和词汇表等长的向量，数值代表该词汇出现在该文档中的次数
 
 
'''
利用python的正则表达式模块re切分句子
@param bigString：文本字符串
''' 
def textParse(bigString):  # input is big string, #output is word list
    import re
    # listOfTokens = re.split(r'\W*', bigString)  # 分隔符是除单词、数字外的任意字符串 (\W* = 分隔符不是单词、数字，\w* = 分隔符是单词、数字)
    listOfTokens = re.split(r'\W+', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]  # 去除长度小于3的字符串（包括空字符串，如末尾有句号的就会产生空字符串）
 
 
'''
使用朴素贝叶斯过滤垃圾邮件
''' 
def spamTest():
    # docList 是文档集合（相当于前面的dataSet），fullText 是所有文档中的词汇，classList 是分类类别
    docList = [];
    fullText = [];
    classList = []
    # 导入并解析文本文件
    for i in range(1, 26):  # [1,26)
        # print(open('email/spam/%d.txt' % i).read())
        wordList = textParse(open('email/spam/%d.txt' % i).read())  # spam（垃圾）类邮件
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())  # ham类邮件
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)  # 创建词汇表
    trainingSet = list(range(50))  # 训练集，是一个整数列表，范围是[0, 50)。用list转化是因为python3中range会返回range对象，而不是列表
    testSet = []  # 创建的一个大小为10的测试集
    for i in range(10):  # 从50个训练文档中随机选择10个文档作为测试集
        randIndex = int(random.uniform(0, len(trainingSet)))  # random.uniform 在[0,50) 内随机生成一个实数，然后将其转化为整数
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])  # 支持list对象删除元素，而不支持range对象删除，故将range改成list
    trainMat = [];
    trainClasses = []
    # 利用剩下的40篇文档训练分类器
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    # 对10篇文档进行分类测试，统计出错概率
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        # print(vocabList)
        print("classList[docIndex]", classList[docIndex], "判断结果：", classifyNB(array(wordVector), p0V, p1V, pSpam))
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print("docIndex:", docIndex, "第几个文件：:", docIndex / 2, "classification error", docList[docIndex])
    print('\nthe error rate of spam email is: ', float(errorCount) / len(testSet))
    print('\nthe error rate of spam email is: ', '{:.2f}%'.format(float(errorCount) / len(testSet) * 100))
 
    # return vocabList,fullText
 
 
spamTest()  # 测试10篇文档的出错率
 
'''
得到高频出现的前30个词汇，因为高频出现的30个词汇可能是无意义的助词等辅助性词汇，之后要把它们删除
@param vocabList：词汇表
@param fullText：所有文档中的词汇
''' 
def calcMostFreq(vocabList, fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)  # 统计词汇表中的每一个单词在所有文档中出现的次数
    sortedFreq = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]  # 返回一个包含频率最高的30个词汇的字典，key=词汇，value=该词汇的次数
 
 
'''
使用朴素贝叶斯从个人广告中获取区域倾向
@param feed1：属于第一类的RSS文件
@param feed0：属于第二类的RSS文件
''' 
def localWords(feed1, feed0):
    import feedparser
    docList = [];
    classList = [];
    fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))  # 取两个RSS源(xml文件数量)中的最小值
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)  # NY是类别1
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    # 移除频率最高的30个词汇，可以删除以下3行代码，观察错误率和输出的频率最高的词汇
    top30Words = calcMostFreq(vocabList, fullText)
    for pairW in top30Words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])  # pairW[0] 是词汇，pairW[1] 是词汇出现次数
    trainingSet = list(range(2 * minLen));
    testSet = []
    # 随机选取20个作为测试集       
    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
    trainMat = [];
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print('\nthe error rate of RSS is: ', float(errorCount) / len(testSet))
    return vocabList, p0V, p1V
 
 
if __name__ == '__main__':
    testingNB()  # ['love', 'my', 'dalmation'] classified as:  0      ['stupid', 'garbage'] classified as:  1
    spamTest()  # 测试10篇文档的出错率