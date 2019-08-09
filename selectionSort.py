list1=list(map(int,input().split()))

for i in range(len(list1)):
    minVal=list1.index(min(list1[i:]))
    # print(list1[minVal])
    if list1[i]>list1[minVal]:
        list1[i],list1[minVal]=list1[minVal],list1[i]
print(list1)    
