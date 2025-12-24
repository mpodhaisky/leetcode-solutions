class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int s = accumulate(apple.begin(), apple.end(), 0);
        
        priority_queue<int> pq(capacity.begin(), capacity.end());
        
        int cnt = 0;
        while (s > 0) {
            s -= pq.top();
            pq.pop(); 
            cnt++;
        }
        return cnt;
    }
};