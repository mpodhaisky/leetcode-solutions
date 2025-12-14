class BIT:
    def __init__(self,N):
        self.length=N+1
        self.stree = [0]*(N+1)
    
    def increase(self,i,x):
        while i<self.length:
            self.stree[i]+=x
            i |= (i+1)
    
    def total(self, i):
        s = 0

        while i>=0:
            s+=self.stree[i]
            i &= i+1
            i-=1
        return s