#!/usr/bin/python
  
import numpy as np
import matplotlib.pyplot as plt
fp = open('key_stat.xyz')
keys = []
stats = []
total = 0
for line in fp:
    x, y = line.split()
    x = x.replace('Key.','').replace(':','')
    keys.append(x)
    stats.append(int(y))
    total += int(y)
print(total)
 
plt.bar(keys,stats)
plt.xticks(keys,rotation='45')
plt.show()