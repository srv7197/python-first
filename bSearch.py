def bSearch(list1, k, l, r):
	mid=(r+l)//2
	if r-l<=1:
		return -1
	if list1[mid]== k:
		return mid
	if list1[mid]<k:
		return bSearch(list1, k, mid, r)
	else :
		return bSearch(list1, k, l, mid)
