class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N,M = len(nums1), len(nums2)
        @cache
        def dp(i,j, is_empty):
            if i >=N or j >=M: return 0 if not is_empty else -inf
            return max(nums1[i]*nums2[j]+dp(i+1,j+1,False),dp(i,j+1,is_empty),dp(i+1,j,is_empty))

        return dp(0,0,True)
        