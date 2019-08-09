listA= list(map(int,input().split()))

def merge(list1, list2):
    c=[]
    m=len(list1)
    n=len(list2)
    i=0
    j=0
    for _ in range(m+n):
        if i==m:
            c.extend(list2[j:])
            break
        elif j==n:
            c.extend(list1[i:])
            break
        elif list1[i]<=list2[j]:
            c.append(list1[i])
            i+=1
        else:
            c.append(list2[j])
            j+=1
    return c
            
def mergeSort(list1):
    n=len(list1)
    if len(list1)==1:
        return list1
    else:
        a=mergeSort(list1[:n//2])
        b=mergeSort(list1[n//2:])
        return merge(a,b)
listA=mergeSort(listA)
print(listA)
    
