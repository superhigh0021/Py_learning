fp=open(input(''),'r+')
str=fp.read()
print(str)
new_str=''
new_str=str.swapcase()
print()
print(new_str)
fp.write(new_str)
fp.close()