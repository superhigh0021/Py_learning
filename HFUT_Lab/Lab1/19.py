import re
str=input("Please enter a string: ")
pattern_str='\\b\\w{3}\\b'
ll=re.findall(pattern_str,str)
print(ll)