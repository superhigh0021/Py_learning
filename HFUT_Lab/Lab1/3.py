Lresult=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k :
                result = i*100+j*10+k
                print('%d '%result,end='')
                Lresult.append(result)
print("\nThe total number is %d"%len(Lresult))