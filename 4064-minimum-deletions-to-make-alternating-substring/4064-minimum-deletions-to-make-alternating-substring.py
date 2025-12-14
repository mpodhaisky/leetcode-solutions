class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        bt, ans = 0, []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                bt |= 1 << i
        for q in queries:
            if q[0] == 1:
                bt ^= 3 << q[1] >> 1
            else:
                ans.append(((bt ^ bt >> q[2] << q[2]) >> q[1]).bit_count())
        return ans