#水果统计A
from random import choice
def countOneFruit():
    fruit={'香蕉':0,'草莓':0,'苹果':0,'梨子':0,'西瓜':0,'芒果':0,'葡萄':0}
    fruit_list=[item for item in fruit.keys()]
    for _ in range(100):
	    pick=choice(fruit_list)
	    fruit[pick]+=1
    print('第{}次共得到{}个苹果'.format(index,fruit['苹果']))

if __name__=='__main__':
    for index in range(1,4):
        countOneFruit()