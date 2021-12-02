import re
fp=open(r'D:\asm\2-1.txt','r')
str=fp.read()
fp.close()
fp=open(r'D:\asm\2-1.txt','w')
for item in str:
    if item.islower():
        fp.write(item.upper())
    else:
        fp.write(item.lower())