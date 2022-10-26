lst=[6,5,8,1,4]
for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
for i in range(0,len(lst)):
    print(lst[i])