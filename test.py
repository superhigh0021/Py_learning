import random #导入随机库，用于随机大素数的生成
import hashlib #哈希值暂时通过调用库来计算
import math

#快速模幂运算
def modPow(a, m, n):
    d = 1
    while m :
        if m & 1: # 如果m & 1=1,那么其二进制形式的最后一位等于1
            d = (d * a) % n
        m >>= 1   # 每一轮右移一位，就能得出其二进制每位是0还是1
        a = (a * a) % n
    return d

#生成大素数
#生成1024 bit长的随机奇数
def genRandOdd(bit):
    oddList = [] #存放奇数位数
    oddList.append('1')  #最高位定为1
    for _ in range(bit-2):
        c = random.choice(['0', '1'])
        oddList.append(c)
    oddList.append('1') # 最低位定为1，这样它必定是奇数
    odd = int(''.join(oddList),2) #将生成的素数转化为10进制数
    return odd

#Miller-Rabin算法检测该奇数是否为素数
def miller_rabin(a,n):
    #首先排除比较明显的合数
    primeLs=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)# 100以内的素数
    for y in primeLs:
        if n % y==0:
            return False
    #利用随机生成的a，用Miller-Rabin算法对n进行检测
    if modPow(a, n-1, n) == 1: # 费马定理，如果a^(n-1)!= 1 mod n, 说明为合数
        d = n-1 # n-1 = (2^q )* m, 求q和m的值，用来判断二次定理
        q = 0
        while not(d & 1):
            q = q+1
            d >>= 1
        m = d
        for i in range(q): # 0~q-1, 我们先找到的最小的a^u，再逐步扩大到a^((n-1)/2)
            u = m * (2**i)
            tmp = modPow(a, u, n)
            if tmp == 1 or tmp == n-1: # 如果满足，则a^(n−1) = 1 (mod n)有解。
                # 满足条件
                return True
        return False
    else:
        return False

#进行k次素性测试
def prime_test(n, k): # 产生k个a
    while k > 0:
        a = random.randint(2, n-1)
        if not miller_rabin(a, n): # 如果返回False，说明这不是个素数，不用继续测试了
            return False
        k = k - 1
    return True

#素数的生成
def genBigPrime():
    while True:
        primeNum = genRandOdd(40) # 产生bit位的素数
        for i in range(50):  # 伪素数附近50个奇数都没有真素数的话，重新再产生一个伪素数
            u = prime_test(primeNum, 12) # 检验12个a来判断产生的是不是素数
            if u:
                break
            else:
                primeNum = primeNum + 2*(i)
        if u:
            return primeNum
        else:
            continue

#扩展的欧几里得算法，检测e和(p-1)*(q-1)是否互素
def exgcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b==1

def Inverse(x, n):
    x0 = x
    y0 = n
    x1 = 0
    y1 = 1
    x2 = 1
    y2 = 0
    while n != 0:
        q = x // n
        (x, n) = (n, x % n)
        (x1, x2) = ((x2 - (q * x1)), x1)
        (y1, y2) = ((y2 - (q * y1)), y1)
    if x2 < 0:
        x2 += y0
    if y2 < 0:
        y2 += x0
    return x2

def RSA_Sig(m,p,q): #输入为待签名明文（哈希值），选择的两个大素数p和q
    n=p*q #公开模n
    euler=(p-1)*(q-1) #欧拉值
    #选择e
    while True:
        e=65537 #初定为65537 可能这样不安全容易猜
        if exgcd(e,euler):
            break
        else:
            e-=1
    #生成d
    d=Inverse(e,euler)
    #签名
    sig=modPow(m,d,n) #私钥加密，公钥解密
    return e,n,sig

def RSA_Ver(m,sig,e,n): #e和n为公开钥
    digest=int(eval('{}{}'.format('0x',hashlib.sha1(str(m).encode('utf-8')).hexdigest()))) #自己计算一次发来的m的哈希值
    digest=digest%n
    ver=modPow(sig,e,n) #把收到的签名用对方的公钥解密，得到哈希值
    return digest == ver

#DH密钥交换
#找一个原根,g^(p-1) = 1 (mod p)当且仅当指数为p-1的时候成立
def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

def factor(euler):
    ls=[]
    for i in range (2,int(math.sqrt(euler)+1)):
        if isPrime(i):
            while euler%i==0:
                ls.append(i)
                euler/=i
    return list(set(ls))

def genPrimRoot(p):
    a=2
    i=1
    euler=p-1
    factors=factor(euler)
    while a<p:
        flag=1
        for k in factors:
            n=int(euler/k)
            if modPow(a,n,p)==1:
                flag=0
                break
        if flag==1:
            return a
        a+=1

def against_MITMA():
    print("-----------------DH密钥交换-----------------")
    print("-全局公开：DH交换的模p,DH交换的原根g,Alice的公开密钥对（pubKeyA,nA),Bob的公开密钥对（pubKeyB，nB)")
    print("-假设中间人Eve可以：生成自己的私钥XE1、XE2并计算相应的YE1、YE2，分别与Alice、Bob进行交换，\n但不可以截获全局公开的参数")
    print("正在生成用于DH密钥交换的大素数模....")
    p=genBigPrime() #生成DH交换的大素数模
    print("模p为:{}".format(p))
    g=genPrimRoot(p) #找到p的原根
    print("正在生成用于DH密钥交换的原根....")
    print("模p的原根为:{}".format(g))

    #Alice产生私钥
    print("正在生成Alice的私钥XA....")
    XA=genBigPrime()
    while XA>=p:
        XA=genBigPrime()
    print("Alice的私钥XA={}".format(XA))

    #Bob产生私钥
    print("正在生成Bob的私钥XB....")
    XB=genBigPrime()
    while XB>=p or XA==XB:
        XB=genBigPrime()
    print("Bob的私钥XB={}".format(XB))

    #计算Alice要发送的数
    YA=modPow(g,XA,p)
    print("Alice计算YA=g^XA mod p={}".format(YA))

    #计算Bob要发送的数
    YB=modPow(g,XB,p)
    print("Bob计算YB=g^XB mod p={}".format(YB))

    #Alice对YA进行签名
    p1=genBigPrime()
    q1=genBigPrime()
    Alice_digest = int(eval('{}{}'.format('0x',hashlib.sha1(str(YA).encode('utf-8')).hexdigest())))
    Alice_digest=Alice_digest%(p1*q1) #模不够大，哈希值被缩短，为了好跑先模，如果多等一会儿可以生成很大的模
    pubKeyA,nA,Alice_Sig = RSA_Sig(Alice_digest, p1,q1)
    print("Alice对YA进行签名，并将YA与签名一起发送给Bob。")
    print("Alice的签名为：{}".format(Alice_Sig))

    #Bob对YB进行签名
    p2=genBigPrime()
    q2=genBigPrime()
    Bob_digest = int(eval('{}{}'.format('0x',hashlib.sha1(str(YB).encode('utf-8')).hexdigest())))
    Bob_digest=Bob_digest % (p2*q2)
    pubKeyB,nB,Bob_Sig = RSA_Sig(Bob_digest, p2,q2)
    print("Bob对YB进行签名，并将YB与签名一起发送给Alice。")
    print("Bob的签名为：{}".format(Bob_Sig))

    #Alice对Bob的签名进行验证
    Alice_Ver_Bob=RSA_Ver(YB,Bob_Sig,pubKeyB,nB)#Bob的公钥，p2*q2

    #Bob对Alice的签名进行验证
    Bob_Ver_Alice=RSA_Ver(YA,Alice_Sig,pubKeyA,nA)

    #验证结果
    print("Alice验证Bob的YB为：{}".format(Alice_Ver_Bob))
    print("Bob验证Alice的YA为：{}".format(Bob_Ver_Alice))
    if Alice_Ver_Bob==True and Bob_Ver_Alice==True:
        print("验证成功！")
        # 输出Alice与Bob交换的密钥
        k = modPow(YB, XA, p)
        print("Alice与Bob交换的密钥为：{}".format(k))
        print("\n")
    else:
        print("验证失败！")
        k1 = modPow(YB, XA, p)
        k2=modPow(YA, XB, p)
        print('Alice算得的密钥：{}   Bob算得的密钥：{}'.format(k1,k2))