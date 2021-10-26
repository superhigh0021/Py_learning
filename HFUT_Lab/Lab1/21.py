def binary_search(llist,target):
    index_i=0
    index_j=len(llist)-1
    while(index_i<=index_j):
        index_mid=int((index_i+index_j)/2)
        if llist[index_mid]==target:
            print(f"The position is {index_mid}")
            return True
        elif llist[index_mid]<target:
            index_i=index_mid+1
        else:
            index_j=index_mid-1
    else:
        return False

llist=[1,2,3,4,5,6,7,8,9,10]
while True:
    target=int(input("Please enter your target: "))
    binary_search(llist,target)