class Solution:
    def countDigitOne(self, n: int) -> int:
        arr = list(map(int,list(str(n))))
        @cache
        def dp(i,is_tight,is_zero):
            if i >= len(arr): return 0, not is_zero
            res=nums=0
            for digit in range(10 if not is_tight else arr[i] + 1):
                a, b = dp(i+1,is_tight and digit==arr[i],is_zero and digit==0)
                res += a + (b if digit ==1 else 0)
                nums+=b
            return res, nums
        return dp(0,True,True)[0]