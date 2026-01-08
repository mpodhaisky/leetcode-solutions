class Solution {
public:
    int dp[501][501][2];
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int N = nums1.size();
        int M = nums2.size();

        memset(dp,0xc0, sizeof(dp));

        for (int i = 0; i<=M; i++) 
            dp[N][i][0] = 0;
        
        for (int i = 0; i<= N; i++)
            dp[i][M][0]=0;
        
        for (int i = N-1; i>=0; i--)
            for (int j=M-1; j>=0; j--)
                for (int k =0; k<2; k++) 
                    dp[i][j][k] = max(
    max(dp[i+1][j][k], dp[i][j+1][k]),
    nums1[i]*nums2[j] + dp[i+1][j+1][0]
);
        return dp[0][0][1];

    }
};