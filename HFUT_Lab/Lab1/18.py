str=input("Please input a txt_string: ")
ll=str.split(' ')
dict=dict()
for item in ll:
    if dict.get(item,0)!=0:
        dict[item]+=1
    else:
        dict[item]=1
print(dict)