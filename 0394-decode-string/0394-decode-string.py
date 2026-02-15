class Solution:
    def decodeString(self, s: str) -> str:
        cur=[""]
        for c in s:
            if "a"<=c<="z":
                cur[-1]+=c
            elif c =="[":
                cur.append("")
            elif c == "]":
                tmp = cur.pop() * int(cur.pop())
                cur[-1]+=tmp
            elif cur[-1].isnumeric():
                cur[-1]+=c
            else:
                cur.append(c)

        return cur.pop()