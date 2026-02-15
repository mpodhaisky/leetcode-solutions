class Solution:
    def minOperations(self, n: int) -> int:
        N = min(1<<i for i in range(40) if (1<<i)>n)
        seen={n}
        q= [(0,n)]
        for step, n in q:
            if n == 0: return step
            for i in range(40):
                m1, m2 = n+(1<<i), n-(1<<i)
                if  m1<= N and m1 not in seen:
                    seen.add(m1)
                    q.append((step+1,m1))
                if m2 >=0 and m2 not in seen:
                    seen.add(m2)
                    q.append((step+1,m2))


        