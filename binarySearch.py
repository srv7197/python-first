list1=list(range(10000000))


k=5696857
l=0
r=len(list1)-1
while(r-l):
    mid=(r+l)//2
    if (r-l)==1:
        if list1[l]==k:
            print(l)
            break
        elif list1[r]==k:
            print(r)
            break
        else:
            print ("not found")
            break
    if list1[r]<k or list1[l]>k:
        print("not found")
        break
    elif list1[mid]==k:
        print(mid)
        break
    elif list1[mid]>k:
        r=mid
    else:
        l=mid

    
