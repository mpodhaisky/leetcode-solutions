class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        strToNum =lambda A: [ord(c)-ord("a") for c in A]
        dp = [[(inf if i!=j else 0) for i in range(26)] for j in range(26)]
        
        for a, b, c in zip(strToNum(original),strToNum(changed),cost):
            dp[a][b]=min(dp[a][b],c)
        
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    dp[j][k]= min(dp[j][k],dp[j][i]+dp[i][k])
        
        res = sum(dp[a][b] for a, b in zip(strToNum(source),strToNum(target)))

        return res if res < inf else -1