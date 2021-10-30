import re
str='高数:89'
list=re.findall('(?<=:).+',str)
print(list)