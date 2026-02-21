class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                delta = pow(x1-x2,2) + pow(y1-y2,2)
                if r1*r1 >= delta:
                    adj[i].append(j)
                if r2*r2>=delta:
                    adj[j].append(i)
        res=0
        for i in range(len(bombs)):
            q= [i]
            seen = set(q)
            for n in q:
                for m in adj[n]:
                    if m not in seen:
                        seen.add(m)
                        q.append(m)
            res = max(res,len(seen))
        return res