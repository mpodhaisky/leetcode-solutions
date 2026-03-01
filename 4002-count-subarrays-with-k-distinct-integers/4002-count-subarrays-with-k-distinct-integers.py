class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        seen = Counter()
        lo=res=cnt=bonus=0
        valid = []
            
        for i,n in enumerate(nums):
            seen[n]+=1
            if seen[n] == m: cnt+=1
            while len(seen) > k:
                bonus=0
                seen[nums[lo]]-=1
                if seen[nums[lo]]==m-1: cnt-=1
                if not seen[nums[lo]]:
                    del seen[nums[lo]]
                lo+=1
            
            if cnt==k:
                while seen[nums[lo]]>m:
                    seen[nums[lo]]-=1
                    lo+=1
                    bonus+=1
                res += 1+bonus

        return res