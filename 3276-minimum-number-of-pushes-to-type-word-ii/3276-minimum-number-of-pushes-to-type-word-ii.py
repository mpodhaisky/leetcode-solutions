class Solution:
    def minimumPushes(self, word: str) -> int:
        i=1
        cnt=0
        res=0
        for v in sorted(Counter(word).values())[::-1]:
            cnt+=1
            if cnt == 9:
                cnt-=8
                i+=1
            res+=v*i
        return res