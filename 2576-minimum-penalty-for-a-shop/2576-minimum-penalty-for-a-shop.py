class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best=cur = customers.count("N")
        res=len(customers)
        for i in range(len(customers)-1,-1,-1):
            cur+=1 if customers[i]=="Y" else -1
            if cur <=best:
                best=cur
                res=i
        return res