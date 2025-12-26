class Solution {
public:
    int bestClosingTime(string cust) {
        int cur=0, res=cur, idx=res;
        for (int i = 0; i < cust.size() ; i++) {
            cur += (cust[i] == 'Y' )? -1 : 1;
            if (cur < res) {
                res = cur;
                idx = i+1;
            }
        }
        return idx;
    }
};