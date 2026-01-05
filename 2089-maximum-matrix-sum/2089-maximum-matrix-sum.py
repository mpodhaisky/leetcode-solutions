class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        parity=reduce(xor,[n<0 for n in chain(*matrix)])
        vals = [abs(n) for n in chain(*matrix)]
        return sum(vals) if not parity else sum(vals)-2*min(vals)