class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def cmp(a,b):
            A, B =(pow(10,len(str(b)))-1)*a , b*(pow(10,len(str(a)))-1)
            if A > B:
                return 1
            elif B>A:
                return -1
            else: return 0

        return str(int("".join(map(str,sorted(nums,key=cmp_to_key(cmp),reverse=True)))))