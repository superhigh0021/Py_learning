fp=open('eng_text.txt','r+')
str=fp.read()
print(str)
new_str=''
for item in str:
    if item.islower():
        item=item.upper()
    elif item.isupper():
        item=item.lower()
    new_str+=item
print(new_str)
fp.write(new_str)
fp.close()