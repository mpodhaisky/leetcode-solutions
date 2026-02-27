from sortedcontainers import SortedList
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        N = len(s) 
        ones = s.count("1")

        rem = [SortedList(range(0,N+1,2)),SortedList(range(1,N+1,2))]
        def adj(ones):
            A = k-min(k,N-ones)
            B = min(ones,k)
            return sorted(ones + k-2*i for i in (A,B))

        q = [(0,ones)]
        for step, n in q:
            if n == N: return step
            lo, hi = adj(n)
            R = range(rem[lo&1].bisect_left(lo),rem[lo&1].bisect_right(hi))
            for m in R[::-1]:
               q.append((step+1,rem[lo&1][m]))
               rem[lo&1].remove(rem[lo&1][m])
        return -1
        
