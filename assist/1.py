#这个是原题 这个版本稍微优雅一点
from random import choice
fruit={'香蕉':0,'草莓':0,'苹果':0,'梨子':0,'西瓜':0,'芒果':0,'葡萄':0}
fruit_list=[item for item in fruit.keys()]
for i in range(100):
	pick=choice(fruit_list)
	fruit[pick]+=1
print(fruit)