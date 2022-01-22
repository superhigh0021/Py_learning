#文本框的题目
from tkinter import*
from random import choice

def onefruit(one_fruit):
    fruit={'香蕉':0,'草莓':0,'苹果':0,'梨子':0,'西瓜':0,'芒果':0,'葡萄':0}
    fruit_list=[item for item in fruit.keys()]
    for _ in range(100):
	    pick=choice(fruit_list)
	    fruit[pick]+=1
    print('随机100次共得到{}个{}'.format(fruit[one_fruit],one_fruit))
    text.insert('insert','随机100次共得到{}个{}\n'.format(fruit[one_fruit],one_fruit))

def run():
    onefruit(entry.get())

root =Tk()
root.title('用户登录界面')

label = Label(root, text='请在输入框中输入任意水果名：')
label.pack()

entry = Entry(root) 
entry.pack()

buttons =Button(root, text='提交', command=run)
buttons.pack()
text=Text(root,height=10)
text.pack()

mainloop()