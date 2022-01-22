#水果统计C
from random import choice
def countSelectedFruit(onefruit,twofruit,*otherfruits):
    fruit={'香蕉':0,'草莓':0,'苹果':0,'梨子':0,'西瓜':0,'芒果':0,'葡萄':0}
    fruit_list=[item for item in fruit.keys()]
    for i in range(100):
        pick=choice(fruit_list)
        fruit[pick]+=1
    #list作打印用
    list=[onefruit,twofruit]
    sum=fruit[onefruit]+fruit[twofruit]
    for index in range(len(otherfruits)):
        sum+=fruit[otherfruits[index]]
        list.append(otherfruits[index])
    #直接打印列表不美观 打印字符串美观一点
    fruit_str=','.join(list)
    print('第{}次共得到{}个{}'.format(flag,sum,fruit_str))
    
if __name__=='__main__':
    flag=1
    countSelectedFruit('香蕉','草莓','苹果')
    flag+=1
    countSelectedFruit('苹果','梨子','西瓜','芒果')
    flag+=1
    countSelectedFruit('草莓','苹果','梨子','西瓜','芒果')