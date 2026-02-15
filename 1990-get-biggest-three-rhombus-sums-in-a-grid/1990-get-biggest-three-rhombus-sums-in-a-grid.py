class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M,N = len(grid), len(grid[0])
        vals=set()

        for r in range(M):
            for c in range(N):
                vals.add(grid[r][c])
                q=[(r,c)]
                seen={(r,c)}
                for _ in range(min(r,c,M-1-r,N-1-c)):
                    cur=0
                    next_q=[]
                    for cr, cc in q:
                        for dr ,dc in ((1,0),(0,1),(0,-1),(-1,0)):
                            nr, nc = cr+dr, cc+dc
                            if 0<=nr<M and 0<=nc<N and (nr,nc) not in seen:
                                seen.add((nr,nc))
                                cur+=grid[nr][nc]
                                next_q.append((nr,nc))
                    vals.add(cur)
                    q = next_q
        return nlargest(3,vals)

                    
                    

                    