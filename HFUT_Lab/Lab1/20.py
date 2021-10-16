import re
str='a:1*a1:2*a2:3*a3:4'
pattern_str='(\*)'
new_str=re.sub(pattern_str,' ',str)
print(new_str)
