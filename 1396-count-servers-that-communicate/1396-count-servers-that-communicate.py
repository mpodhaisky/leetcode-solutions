class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        rows = [sum(row) >= 2 for row in grid]
        cols = [sum(col) >= 2 for col in zip(*grid)]
        return sum(rows[r] | cols[c] for r, c in product(range(M),range(N)) if grid[r][c])