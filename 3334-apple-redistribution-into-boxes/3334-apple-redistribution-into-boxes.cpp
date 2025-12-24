class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int s = accumulate(apple.begin(),apple.end(),0);
        int cnt=0;
        make_heap(capacity.begin(),capacity.end());
        while (s>0) {
            pop_heap(capacity.begin(),capacity.end());
            s-=capacity.back();
            capacity.pop_back();
            cnt++;
        }
        return cnt;
    }
};