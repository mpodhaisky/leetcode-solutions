class Solution:
    def numOfWays(self, n: int) -> int:
        M=10**9+7
        dp={"333":1}
        for _ in range(n):
            next_dp=Counter()
            for row in dp:
                for a, b, c in product(map(str,range(3)),repeat=3):
                    if a!=b and b!=c and a!=row[0] and b!=row[1] and c!=row[2]:
                        next_dp[a+b+c]=(next_dp[a+b+c]+dp[row])%M
            dp=next_dp
        return dp.total() % M
