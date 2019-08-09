import math
class heap:
    hp=[]
    def __init__(self, hp=[]):
        self.hp=hp
        self.stablize()

    def show(self):
        return self.hp

    def noOfLevels(self):
        k=math.log(len(self.hp)+1,2)
        if k==math.floor(k):
            return int(k)
        else:
            return math.floor(k)+1

    def stablize(self):
        k=self.noOfLevels()
        for i in range(k-2,-1,-1):
            for j in range((2**i)-1,(2**(i+1))-1):
                self.stablizeAt(j)

    def stablizeAt(self,k):
        left=2*k+1
        right=2*k+2
        if left<len(self.hp) and(self.hp[left]>self.hp[k]) or right<len(self.hp) and(self.hp[right]>self.hp[k]):
            if left<len(self.hp)and(self.hp[left]>self.hp[k]):
                if right>=len(self.hp):
                    self.hp[k],self.hp[left]=self.hp[left],self.hp[k]
                    return
                elif right<len(self.hp) and (self.hp[left]>self.hp[right]):
                    self.hp[k],self.hp[left]=self.hp[left],self.hp[k]
                    self.stablizeAt(left)
                elif right<len(self.hp) and (self.hp[left]<self.hp[right]):
                    self.hp[k],self.hp[right]=self.hp[right],self.hp[k]
                    self.stablizeAt(right)
            elif right<len(self.hp) and (self.hp[right]>self.hp[k]):
                if left>=len(self.hp):
                    self.hp[k],self.hp[right]=self.hp[right],self.hp[k]
                    return
                elif left<len(self.hp) and (self.hp[right]>self.hp[left]):
                    self.hp[k],self.hp[right]=self.hp[right],self.hp[k]
                    self.stablizeAt(right)

        else:
            return

    def deleteMax(self):
        self.hp[0],self.hp[-1]=self.hp[-1],self.hp[0]
        self.hp.pop()
        self.stablizeAt(0)

    def insert(self,x):
        k=self.noOfLevels()
        self.hp.append(x)
        j=len(self.hp)-1
        for i in range(k-2,-1,-1):
            self.stablizeAt((j-1)//2)
            j=(j-1)//2
    
            
                    

                        
