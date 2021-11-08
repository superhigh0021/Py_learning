# -*- coding: utf-8 -*-


import base64
import time
import json
import re
import requests
import os
import Crypto.PublicKey.RSA
import Crypto.Cipher.PKCS1_v1_5

"""
第一部分：获取用户长江雨课堂相应试卷的课程Id和课堂Id
"""
#对密码进行RSA加密
def RSA_PSW(pwd):
    try:
        public_key = "-----BEGIN PUBLIC KEY-----\nMIGJAoGBAJAFo9ftysQfr+NLiFEPuVmuwVEh1/ASEffSicWeudbGJEBPM/1YSd5c\nkRkeimbO52Q1LlsOnnVIKcFQYaB8v+xRSuWuFXbGdNJ7WNGX3bh6NXmuRWSKKLzm\nOn0bx4msk3qSUezQ99h+ngRUnzrzyqmLmIRO2D6rghOhzITIPX7vAgMBAAE=\n-----END PUBLIC KEY-----"
        y = pwd.encode(encoding="utf-8")
        b = public_key.encode(encoding="utf-8")
        cipher_public = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(b))
        #使用长江雨课堂公钥进行加密
        cipher_text = cipher_public.encrypt(y)
        text = base64.b64encode(cipher_text).decode(encoding="utf-8")
        return text
    except:
        return False
    
#登录长江雨课堂
def login(tel,pwd):
    url = 'https://changjiang.yuketang.cn/pc/login/verify_pwd_login/'
    data = {
            "type":"PP",
            "name":tel,
            "pwd":pwd
    }
    headers={
            'Connection': 'keep-alive',
            'Content-Language':'zh-cn',
            'Content-Type': 'text/html; charset=utf-8',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'changjiang.yuketang.cn',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36'
    }
    try:
        session = requests.session()
        cookie_jar = session.post(url=url,json=data,headers=headers,verify=False).cookies
        cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
        cookieStr = "csrftoken=" + cookie_t['csrftoken'] + ";" + "sessionid=" + cookie_t['sessionid']
        return cookieStr
    except:
        return False

def smlogin(cookieinfo):
    try:
        cookie_t = cookieinfo
        cookieStr = "csrftoken=" + cookie_t['csrftoken'] + ";" + "sessionid=" + cookie_t['sessionid']
        return cookieStr
    except:
        return False
    
#查找课程的信息
def showCourse(cookieStr):
    cookie = cookieStr
    url = "https://changjiang.yuketang.cn/v/course_meta/my_courses?_date="
    curtime = "{0:.3f}".format(float(time.time())).replace(".","")
    url += curtime
    try:
        headers={
            'accept':'*/*',
            'accept-language':'zh-CN,zh;q=0.9',
            'connection':'keep-alive',
            'referer':url,
            'Cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers,verify=False)
        courseinfo = response.json()
        return courseinfo['data']['classrooms']
    except:
        return False

#提取课程关键信息     
def getCourse(courseinfo):
    course_list = []
    try:
        for elem in courseinfo:
            elem_list = []
            courseName = elem['course']['name'] + ","              #课程名
            courseId = str(elem['course']['id']) + ","             #course_id
            classroomId = str(elem['id']) + ","                    #classroom_id
            studentCount = str(elem['students_count']) + ","       #学生人数
            startTime = elem['time'] + ","                         #开课时间
            university = elem['university_name']             #学校名称
            elem_list.append(courseName)
            elem_list.append(courseId)
            elem_list.append(classroomId)
            elem_list.append(studentCount)
            elem_list.append(startTime)
            elem_list.append(university)
            course_list.append(elem_list)
        return course_list 
    except:
        return False

#将提取课程信息写入文件            
def writeCourseInfo(courselist,url):
    fileadd = url
    dicts = {}
    try:
        fo = open(fileadd,'w')
        suoyin = 1
        for lists in courselist:
            listLen = len(lists)
            for i in range(listLen):
                fo.write(lists[i])
            fo.write("\n")
            dicts[str(suoyin)] = lists[0].replace(',','')
            suoyin += 1
        fo.close()
        return True,url,dicts
    except:
        return False,url,dicts

#读取写入的课程信息文件            
def readCourseInfo(query,url):
    fileadd = url
    queryNUm = query
    course_id = "无"
    classroom_id = "无"
    try:
        fo = open(fileadd,'r')
        data = fo.read().split('\n')
        suoyin = 1
        for lists in data:
            lists = lists.split(',')
            listLen = len(lists)
            for i in range(listLen):
                if(queryNUm == str(suoyin)):
                    course_id = lists[1]
                    classroom_id = lists[2]
            suoyin += 1
        fo.close()
        return True,course_id,classroom_id
    except:
        return False,course_id,classroom_id

#获取所查询课程详细信息
def getDetailQuery(cookie,course_id,classroom_id):
    #获取每门课程考试的Id
    curtime = "{0:.3f}".format(float(time.time())).replace(".","")
    url = "https://changjiang.yuketang.cn/v/course_meta/classroom_logs?course_id=" + course_id + "&classroom_id=" + classroom_id + "&activity_type=-1&date_time=" + curtime
    try:
        headers={
            'accept':'*/*',
            'accept-language':'zh-CN,zh;q=0.9',
            'connection':'keep-alive',
            'referer':url,
            'Cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers,verify=False)
        exam = response.json()
        return exam['data']['activities']
    except:
        return False

#提取所查询课程关键详细信息 
def getExam(queryinfo):
    query_list = []
    try:
        for elem in queryinfo:
            for el in elem:
                if(str(el['type']) == '4'):
                    elem_list = []
                    examTitle = el['title']                     #项目名
                    examId = str(el['id'])                      #项目id
                    quizId = str(el['courseware_id'])           #courseware_id
                    queryType = str(el['type'])                 #类型(Type=4为试卷)
                    elem_list.append(examTitle)
                    elem_list.append(examId)
                    elem_list.append(quizId)
                    elem_list.append(queryType)
                    query_list.append(elem_list)
        return query_list 
    except:
        return False

#获取所要查询试卷加密的题目信息
def getHtml(cookie,query,rawaddr):
    url = "https://changjiang.yuketang.cn/quiz/quiz_info/" +  query + "/"
    try:
        headers={
            'accept':'*/*',
            'accept-language':'zh-CN,zh;q=0.9',
            'connection':'keep-alive',
            'referer':url,
            'Cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers,verify=False)
        exam = response.text
        fo = open(rawaddr,'w')
        fo.write(exam)
        fo.close()
        return True
    except:
        return False

#获取加密字段
def getSecret(rawaddr,dataaddr):
    try:
        fo = open(rawaddr,'r')
        fs = open(dataaddr,'w')
        data = fo.read()
        p = re.compile(r'var quizData = "(.*?)";')
        data = p.findall(data)
        fs.write(data[0])
        fo.close()
        fs.close()
        return True
    except:
        return False
    
"""
第二部分：长江雨课堂对应试卷作答情况解密
"""
#读取加密文件
def readCode(readUrl):
    try:
        url = readUrl
        rcode = open(url,'r')
        code = rcode.readline()
        rcode.close()
        return code
    except:
        return False

#写入解密文件
def writeText(writeUrl,text):
    try:
        url = writeUrl
        wcode = open(url,'w')
        wcode.write(text)
        wcode.close()
        return "写入解密文件完毕"
    except:
        return "写入解密文件失败"

# base64解密
def base64Decode(rawCode):
    try:
        mystr = rawCode
        str_url = base64.b64decode(mystr).decode("utf-8")
        return str_url
    except:
        return False

"""
第三部分：获取试卷题目图片
"""
#获取试卷中所有的图片链接
def getImgUrl(decodeaddr,imgsaveDir):
    try:
        fo = open(decodeaddr,'r')
        data = json.loads(fo.read())
        problemdata = data['Slides']
        dicts = {'0':'题目','1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G'}
        alllist = []
        urllist = []
        for problem in problemdata:
            urllist = []
            suoyin = 0
            try:
                for en in problem['Shapes']:
                    problemlist = []
                    problemlist.append(dicts[str(suoyin)])
                    problemlist.append(en['URL'])                               #获取图片链接
                    urllist.append(problemlist)
                    suoyin += 1
                problemlist = []
                try:
                    Answers = str(problem['Problem']['Answer'])
                    try:
                        if(str(problem['Problem']['analysis']) == "None"):
                            Analysis = "暂无分析"
                        else:
                            Analysis = str(problem['Problem']['analysis'])
                    except:
                        Analysis = "暂无分析"
                    if(Answers == ""):
                        Answers = "答案暂未公布(可能包含在分析中)"
                    problemlist.append('问题ID:' + str(problem['Problem']['ProblemID']))            #获取问题ID
                    problemlist.append('标准答案:' + Answers)                                       #获取答案
                    problemlist.append('我的作答:' + str(problem['Problem']['Result']['Answer']))   #获取我的作答
                    problemlist.append('分析:' + Analysis)                                          #分析(很可能含答案)
                    urllist.append(problemlist)
                    alllist.append(urllist)
                except:
                    alllist.append(urllist)
                    print('这是封面')
            except:
                continue
                
        count = 1
        for url in alllist:
            answerDir = imgsaveDir + '答案.csv'
            if(count == 1):
                #覆盖之前的答案
                fs = open(answerDir,'w')
                fs.write("")
                fs.close()
            fs = open(answerDir,'a+')
            if(len(url) >= 2):
                fs.write(str(url[0][1]) + str(url[-1]) + '\n')
                fs.close()
            elif(len(url) <= 1):
                fs.write('----' + '\n')
            else:
                fs.write(str(url[0][1]) + str(url[1]) + '\n')
                fs.close()
            for i in range(len(url)):
                try:
                    imgName = ""
                    imgUrl = url[i][1]
                    print(imgUrl)
                    imgName += "第" + str(count) + "题"
                    if(len(imgUrl) >= 5 and imgUrl[0:5] == "https"):
                        imgName += str(url[i][0])
                        imgres = requests.get(imgUrl) #取得文件内容
                        imgSaveUrl = imgsaveDir + "{0:0>3}".format(str(count)) + '-' + str(i) + '.png'
                        with open(imgSaveUrl, "wb") as f:
                           f.write(imgres.content)
                           f.close()
                        time.sleep(0.1)
                except:
                    continue
            count += 1
        os._exit(0)
        return True
    except Exception as e:
        print(e)
        return False

"""
第四部分：其他功能相关函数
"""
#创建目录文件夹 
def mkdir(path):
    try:
        # 去除首位空格
        path=path.strip()
        # 去除尾部 \ 符号
        path=path.rstrip("\\") 
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path) 
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path) 
            print(path+'创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path+'目录已存在')
            return False
    except Exception as e:
        print("mkdir(path)--ERROR"+e)
        return False

if __name__ == '__main__':
    cookieinfo = {}
    loginway = str(input('输入0为Cookie登录,输入其他为手机号+密码登录:'))
    #登录方式一:需要自行修改tel(注册电话号码)与pwd(对应加密后的密码)字段的值
    if(loginway != "0"):
        #声明：这种登录方法长久有效，账户信息不变时不需要再次修改或更新
        tel = ""
        password = ""
        pwd = RSA_PSW(password)
        if(pwd != False):
            cookieStr = login(tel,pwd)
        else:
            print('密码加密失败')
            print('程序已自动切换为Cookie登录')
            cookieinfo['csrftoken'] = str(input('请输入csrftoken:'))
            cookieinfo['sessionid'] = str(input('请输入sessionid:'))
            cookieStr = smlogin(cookieinfo)
    #登录方式二:(不要修改任何字段的值)
    else:
        #声明：这种登录方法有时效性，需要及时更新cookieinfo['csrftoken']和cookieinfo['sessionid']的值
        #如输入:928khBplVlPJTqiKWcYvF4PsS3NjgD4O
        cookieinfo['csrftoken'] = str(input('请输入csrftoken:'))
        #如输入:1yjl3t64wefkem71f449s87z94f2a0gx
        cookieinfo['sessionid'] = str(input('请输入sessionid:'))
        cookieStr = smlogin(cookieinfo)
    if(cookieStr == False):
        print('长江雨课堂登录失败')
    else:
        courseinfo = showCourse(cookieStr)
        if(courseinfo == False):
            print('获取课程信息失败')
        else:
            courselist = getCourse(courseinfo)
            if(courselist == False):
                print('提取课程关键要素失败')
            else:
                mkdir(".\\我的课程信息\\")
                haveWrite, courseaddr, coursename = writeCourseInfo(courselist,'我的课程信息/courseInfo.csv')
                if(haveWrite == False):
                    print('课程信息写入文件' + courseaddr + '失败')
                else:
                    print('恭喜课程信息写入成功')
                    course_dicts = {}
                    for course in courselist:
                         course_dicts[course[1].replace(',','')] = course[0].replace(',','')
                    for i in range(len(coursename)):
                        print(str(i + 1),coursename[str(i + 1)])
                    courseQuery = str(input("请输入上述课程名对应的序号:"))
                    haveQuery, course_id, classroom_id = readCourseInfo(courseQuery,'我的课程信息/courseInfo.csv')
                    try:
                        dirName = course_dicts[course_id]
                        mkdir('.\\我的课程信息\\' + dirName + '\\')
                    except:
                        print('课程名与课程ID匹配失败')
                        haveQuery == False
                    if(haveQuery == False):
                        print('课程查询失败')
                    else:
                        detailQuery = getDetailQuery(cookieStr,course_id,classroom_id)
                        if(detailQuery == False):
                            print('获取所查询课程详细信息失败')
                        else:
                            examlist = getExam(detailQuery)
                            if(examlist == False):
                                print('考试信息获取失败')
                            else:
                                for i in range(len(examlist)):
                                    try:
                                        print("{:-<10}----".format(examlist[i][2]),end = "")
                                        print(examlist[i][0])
                                    except:
                                        print('获取第' + str(i+1) + '个考试信息的Id失败')
                                        continue
                                examquery = str(input("请输入上述查询的考试号:"))
                                exam_dicts = {}
                                for exam in examlist:
                                    exam_dicts[exam[2].replace(',','')] = exam[0].replace(',','')   
                                try:
                                    mkdir('.\\我的课程信息\\' + dirName + '\\' + exam_dicts[examquery] + '\\')
                                    rawaddr = '我的课程信息/' + dirName + '/' + exam_dicts[examquery] + '/' + 'rawQuiz-' + examquery + '.txt'
                                    haveHtml = getHtml(cookieStr,examquery,rawaddr)
                                except:
                                    haveHtml = False
                                if(haveHtml == False):
                                    print('获取所要查询试卷加密的题目信息失败')
                                else:
                                    dataaddr = '我的课程信息/' + dirName + '/' + exam_dicts[examquery] + '/' + 'data-' + examquery + '.txt'
                                    haveSecret = getSecret(rawaddr,dataaddr)
                                    if(haveSecret == False):
                                        print('获取加密字段失败')
                                    else:
                                        rawCode = readCode(dataaddr)
                                        if(rawCode == False):
                                            print('读取加密文件失败')
                                        else:
                                            deCode = base64Decode(rawCode)
                                            if(deCode == False):
                                                print('base64解密失败')
                                            else:
                                                writeUrl = '我的课程信息/' + dirName + '/' + exam_dicts[examquery] + '/' + 'decodeText-' + examquery + '.txt'
                                                print(writeText(writeUrl,deCode))
                                                mkdir('.\\我的课程信息\\' + dirName + '/' + exam_dicts[examquery] + '\\图片(含答案)\\')
                                                haveImg = getImgUrl(writeUrl,'我的课程信息/' + dirName + '/' + exam_dicts[examquery] + '/图片(含答案)/')
                                            
