class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(a):
            stack=[]
            for n in a:
                if n not in "()": continue
                if stack and stack[-1]=="(" and n==")":
                    stack.pop()
                else:
                    stack.append(n)

            return not stack
        
        q=[(s,0)]
        seen={s}

        res=[]
        cnt=inf
        for s, steps in q:
            if steps > cnt: continue
            if valid(s):
                res.append(s)
                cnt=steps
                continue
            for i in range(len(s)):
                if s[i] not in "()": continue
                nxt = s[:i]+s[i+1:]
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt,steps+1))
        return res