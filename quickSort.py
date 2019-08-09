list1= list(map(int,input().split()))

def quickSort(list1,l,r):
    if r-l<=1:
        return
    pivot=list1[l]
    separator=l
    indicator=l+1
    while indicator < r:
        if list1[indicator]<pivot:
            list1[indicator],list1[separator+1]=list1[separator+1], list1[indicator]
            indicator+=1
            separator+=1
        else:
            indicator+=1
    list1[l],list1[separator]=list1[separator],list1[l]
    quickSort(list1,l, separator+1)
    quickSort(list1,separator+1,r)

quickSort(list1,0,len(list1))            
print(list1)    
    
