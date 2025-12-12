class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        adj=defaultdict(list)
        for i in range(len(ring)):
            for j, m in enumerate(ring):
                adj[(i,m)].append(j)
            
        dp = [[inf for _ in range(len(key))] + [0 for _ in range(len(key))] for _ in range(len(ring))]

        for j in range(len(key)-1,-1,-1):
            for i in range(len(ring)):
                for neigh in adj[(i,key[j])]:
                    dist = min(len(ring)-abs(neigh-i),abs(neigh-i))
                    dp[i][j]=min(dp[i][j],1+dist+dp[neigh][j+1])
        return dp[0][0]

        # dp[i][j] ring, key