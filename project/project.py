from pickle import FALSE
import qianming as qm
import argparse
from DH import *
def xiaoxi(xiao):
    print("对文字进行数字签名以及验证")
    print("======================================")
    print("签名：")
    #首先生成公钥与私钥
    key=qm.generatePublicAndSecretKeys()
    #公钥
    publickey=[key["e"],key["n"]]
    print("生成的公钥为：{}".format(publickey))
    #私钥
    privatekey=[key["d"],key["n"]]
    print("生成的私钥为：{}".format(privatekey))
    #文字的摘要
    aa=xiao
    print("签名的消息为：{}".format(aa))
    cc=aa.encode("utf-8")
    zhaiyao=qm.hashing(cc)
    print("文字的摘要为：{}".format(zhaiyao))
    print("使用私钥以及文字摘要生成签名：私钥：{}，文字摘要：{}".format(privatekey,zhaiyao))
    #文字生成的签名,使用私钥进行签名
    s=qm.signMessage(zhaiyao,privatekey[0],privatekey[1])
    print("文字生成的签名为：{}".format(s))
    print("验证：")
    print("使用公钥以及签名看生成的摘要内容是否一致：公钥：{}，签名：{}，原本的摘要：{}".format(publickey,s,zhaiyao))
    shencheng=qm.verifySign(s,publickey[0],publickey[1])
    print("检验生成的消息摘要：{}".format(shencheng))
    if shencheng==zhaiyao:
        print("验证成功\n")
        return True
    else:
        print("验证失败\n")
        return FALSE
    print("======================================")

def file(ff):
    print("对文件进行数字签名")
    print("======================================")
    print("签名：")
    #首先生成公钥与私钥
    key=qm.generatePublicAndSecretKeys()
    #公钥
    publickey=[key["e"],key["n"]]
    print("生成的公钥为：{}".format(publickey))
    #私钥
    privatekey=[key["d"],key["n"]]
    print("生成的私钥为：{}".format(privatekey))
    #文件的摘要
    file=open(ff,"rb")#读取文件
    cc=file.read()
    zhaiyao=qm.hashing(cc)
    print("文件的摘要为：{}".format(zhaiyao))
    print("使用私钥以及文字摘要生成签名：私钥：{}，文字摘要：{}".format(privatekey,zhaiyao))
    #文字生成的签名,使用私钥进行签名
    s=qm.signMessage(zhaiyao,privatekey[0],privatekey[1])
    print("文字生成的签名为：{}".format(s))
    print("验证：")
    print("使用公钥以及签名看生成的摘要内容是否一致：公钥：{}，签名：{}，原本的摘要：{}".format(publickey,s,zhaiyao))
    shencheng=qm.verifySign(s,publickey[0],publickey[1])
    print("检验生成的消息摘要：{}".format(shencheng))
    if shencheng==zhaiyao:
        print("验证成功")
    else:
        print("验证失败")
    print("======================================")

def DH_exchange():
     # 得到规定的素数
    flag = False
    while flag == False:
        print('Please input your number(It must be a prime!): ', end='')
        p = input()
        p = int(p)
        flag = judge_prime(p)
    print(str(p) + ' is a prime! ')

    # 得到素数的一个原根
    list = get_generator(p)
    print(str(p) + ' 的一个原根为：', end='')
    print(list[-1])
    print('------------------------------------------------------------------------------')

    # 得到A的私钥
    XA = random.randint(0, p - 1)
    print('A随机生成的私钥为：%d' % XA)

    # 得到B的私钥
    XB = random.randint(0, p - 1)
    print('B随机生成的私钥为：%d' % XB)
    print('------------------------------------------------------------------------------')

    # 得待A的计算数
    YA = get_calculation(p, int(list[-1]), XA)
    print('A的计算数为：%d' % YA)

    # 得到B的计算数
    YB = get_calculation(p, int(list[-1]), XB)
    print('B的计算数为：%d' % YB)
    print('------------------------------------------------------------------------------')

    # 交换后A的密钥
    key_A = get_key(XA, YB, p)
    print('A的生成密钥为：%d' % key_A)

    # 交换后B的密钥
    key_B = get_key(XB, YA, p)
    print('B的生成密钥为：%d' % key_B)
    print('---------------------------True or False------------------------------------')

    print(key_A == key_B)
    return [YA,YB]
if __name__ == '__main__':
    llist = DH_exchange()
    YA_sign = xiaoxi(str(llist[0]))
    YB_sign = xiaoxi(str(llist[1]))

    if YA_sign and YB_sign:
        print('密钥交换成功！')
