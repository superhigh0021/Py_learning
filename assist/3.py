#水果统计B
from random import choice
def countOneFruit(onefruit):
    fruit={'香蕉':0,'草莓':0,'苹果':0,'梨子':0,'西瓜':0,'芒果':0,'葡萄':0}
    fruit_list=[item for item in fruit.keys()]
    for _ in range(100):
	    pick=choice(fruit_list)
	    fruit[pick]+=1
    print('第{}次共得到{}个{}'.format(flag,fruit[onefruit],onefruit))

if __name__=='__main__':
    flag=1
    countOneFruit('香蕉')
    flag+=1
    countOneFruit('草莓')
    flag+=1
    countOneFruit('苹果')