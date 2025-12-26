class Solution {
public:
    int bestClosingTime(string customers) {
        int cur=0, res=0, idx=customers.length();
        for (int i = customers.length()-1; i >=0; i--) {
            cur += (customers[i] == 'Y' )? 1 : -1;
            if (cur <= res) {
                res = cur;
                idx = i;
            }
        }
        return idx;
    }
};