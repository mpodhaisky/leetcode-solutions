class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj=defaultdict(list)
        for i , A in enumerate(accounts):
            for email in A[1:]:
                adj[str(i)].append(email)
                adj[email].append(str(i))
        
        rem=set(map(str,range(len(accounts))))

        res=[]

        while rem:
            
            q=[rem.pop()]
            seen=set(q)
            cur = []
            for n in q:
                if not n.isdigit(): cur.append(n)
                else: rem-={n}
                for m in adj[n]:
                    if m not in seen:
                        seen.add(m)
                        q.append(m)
            
            res.append([accounts[int(q[0])][0]] + sorted(cur))
        return res

