import re
str='a:1*a1:2*a2:3*a3:4'
new_str=re.sub('(\*)',' ',str)
print(new_str)
ll1=re.findall('\w+(?=\:)',new_str)
ll2=re.findall('(?<=\:)\w',new_str)
dic=dict()
for i in range(0,len(ll1)):
    dic[ll1[i]]=ll2[i] 
print(dic)