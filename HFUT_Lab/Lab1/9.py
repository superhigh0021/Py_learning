# abcba
def judge(str):
    list=str
    rlist=list[::-1]
    for index in range(int(len(list)/2)):
        if list[index]!=rlist[index]:
            break;
    else:
        return True
while True:
    str=input("Please input a string: ")
    print(judge(str))