class Solution:
    def validateCoupons(self, A: List[str], B: List[str], C: List[bool]) -> List[str]:
        valid = set(ascii_lowercase+ascii_uppercase+"0123456789_")
        valid_lines = {"electronics":0,"grocery":1,"pharmacy":2,"restaurant":3}
        codes = [(c,line) for c,line,active in zip(A,B,C) if c and not set(c)- set(valid) and line in valid_lines and active]
        codes.sort(key=lambda x: (valid_lines[x[1]],x[0]))
        return [r[0] for r in codes]