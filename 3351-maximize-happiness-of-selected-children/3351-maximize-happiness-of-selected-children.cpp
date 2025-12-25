using ll = long long;
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        make_heap(happiness.begin(),happiness.end());
        ll res = 0;
        for (int i = 0; i<k; i++) {
            pop_heap(happiness.begin(),happiness.end());
            res+=max(0,happiness.back()-i);
            happiness.pop_back();
        }
        return res;
    }
};