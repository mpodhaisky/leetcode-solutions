class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers = [[row.count(c) for c in ascii_lowercase] for row in stickers]
        target = tuple(target.count(c) for c in ascii_lowercase)
        
        @cache
        def dp(mask):
            if not sum(mask): return 0
            mask = list(mask)
            res=inf
            for s in stickers:
                dummy =mask.copy()
                for i, cnt in enumerate(s):
                    dummy[i]=max(0,dummy[i]-cnt)
                if dummy!=mask:
                    res=min(res,dp(tuple(dummy))+1)
            return res
        
        out = dp(target)
        return out if out < inf else -1
