class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        parity=reduce(xor,[n<0 for row in matrix for n in row])
        vals = [abs(n) for row in matrix for n in row]
        return sum(vals) if not parity else sum(vals)-2*min(vals)