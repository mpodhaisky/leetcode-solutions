class SparseTable:
    def __init__(self,arr,op):
        self.st = [arr]
        self.op = op
        for i in range(1,100):
            if (1<<i) > len(arr):
                break
            self.st.append([0]*len(arr))
            for j in range(len(arr)-(1<<i)+1):
                self.st[-1][j] = op(self.st[-2][j],self.st[-2][j+(1<<(i-1))])
    
    def query(self,a,b):
        cur = 0
        while b-a+1 > 1<<(cur+1):
            cur+=1 
        return self.op(self.st[cur][a],self.st[cur][b-(1<<cur)+1])
