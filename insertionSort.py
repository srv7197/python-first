list1= list(map(int,input().split()))

for i in range(1,len(list1)):
    j=i-1
    k=i
    while(j>=0 and list1[j]>list1[k]):
        list1[j],list1[k]=list1[k],list1[j]
        j-=1
        k-=1

print(list1)
