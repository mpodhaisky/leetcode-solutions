#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string s;

    // dp[i][is_tight][even_sum][odd_sum]
    long long memo[20][2][200][200];
    bool vis[20][2][200][200];

    long long dfs(int i, bool is_tight, int even, int odd) {
        if (i == (int)s.size()) {
            return (even != 0 && even == odd) ? 1LL : 0LL;
        }

        if (vis[i][is_tight][even][odd]) {
            return memo[i][is_tight][even][odd];
        }

        long long res = 0;
        int limit = is_tight ? (s[i] - '0') : 9;

        for (int m = 0; m <= limit; m++) {
            bool next_tight = is_tight && (m == limit);

            int next_even = even;
            int next_odd = odd;

            if (i & 1) next_even += m;
            else       next_odd += m;

            res += dfs(i + 1, next_tight, next_even, next_odd);
        }

        vis[i][is_tight][even][odd] = true;
        memo[i][is_tight][even][odd] = res;
        return res;
    }

    long long solve(long long x) {
        if (x < 0) return 0;
        s = to_string(x);
        memset(vis, 0, sizeof(vis));
        return dfs(0, true, 0, 0);
    }

    long long countBalanced(long long lo, long long hi) {
        return solve(hi) - solve(lo - 1);
    }
};
