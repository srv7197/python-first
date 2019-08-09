class sorting:
    l=[]
    def __init__(self,l):
        l=l
    def selection_sorting(self):
        for i in range(len(l)):
            (l[i],min(l[i:]))=(min(l[i:]),l(l[i]))

l1=list(map(int,input().split()))
l2=sorting(l1)
l2.selection_sorting()
