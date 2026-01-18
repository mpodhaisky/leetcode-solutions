class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        @cache
        def fr(r,c): return 0 if c<0 else grid[r][c]+fr(r,c-1)
        @cache
        def fc(r,c): return 0 if r <0 else grid[r][c]+fc(r-1,c)
        @cache
        def fd1(r,c): return 0 if r<0 or c<0 else grid[r][c]+fd1(r-1,c-1)
        @cache
        def fd2(r,c): return 0 if r>=len(grid) or c<0 else grid[r][c]+fd2(r+1,c-1)
        @cache
        def is_magic(r,c,k):
            rows = set(fr(r+i,c+k-1)-fr(r+i,c-1) for i in range(k))
            cols = set(fc(r+k-1,c+i)-fc(r-1,c+i) for i in range(k))
            d1 = fd1(r+k-1,c+k-1)-fd1(r-1,c-1)
            d2 = fd2(r, c+k-1) - fd2(r+k, c-1)
            return len(rows|cols|{d1}|{d2})==1

        res=1
        M, N = len(grid), len(grid[0])
        for r in range(M):
            for c in range(N):
                for k in range(min(N-c,M-r),res,-1):
                    if is_magic(r,c,k):
                        res=k
                        break
        return res