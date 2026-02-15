class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        banned=defaultdict(set)
        for i in range(1,100):
            for j in range(i+1,100):
                if i + j ==k:
                    banned[j].add(i)
        cur = set()

        def ok(x):
            for m in banned[x]:
                if m in cur:
                    return False
            return True
        for i in range(1,100):
            if ok(i):
                cur.add(i)
            if len(cur)==n:
                return sum(cur)