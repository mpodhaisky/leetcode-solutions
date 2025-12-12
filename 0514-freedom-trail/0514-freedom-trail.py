class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        adj=defaultdict(list)
        for i in range(len(ring)):
            for j, m in enumerate(ring):
                adj[(i,m)].append(j)
        last=[0 for _ in range(len(ring))]
        cur = [inf for _ in range(len(ring))]
        for j in range(len(key)-1,-1,-1):
            for i in range(len(ring)):
                for neigh in adj[(i,key[j])]:
                    dist = min(len(ring)-abs(neigh-i),abs(neigh-i))
                    cur[i]=min(cur[i],1+dist+last[neigh])
            cur, last = [inf for _ in range(len(ring))], cur
        return last[0]

        # dp[i][j] ring, key