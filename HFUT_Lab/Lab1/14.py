setA={int(x) for x in input("Please enter a set: ").split(' ')}
print(setA)
setB={int(x) for x in input("Please enter a set: ").split(' ')}
print(setB)
print('setA&setB={}'.format(setA&setB))
print('setA-setB={}'.format(setA-setB))
print('setB-setA={}'.format(setB-setA))
print('setA|setB={}'.format(setA|setB))

llist=list({u for u in input("Please input a set of words:").split(' ')})
llist.sort()
print(llist)