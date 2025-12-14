

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        sl=SortedList()
        lo=0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                sl.add([lo,i-1])
                lo=i
        sl.add([lo,len(s)-1])
        res=[]
        for q in queries:
            if q[0]==1:
                idx = sl.bisect_left([q[1],q[1]])
                if idx==len(sl) or sl[idx][0]>q[1]: idx-=1
                if sl[idx][0]==sl[idx][1]:
                    if idx-1>=0 and idx+1<len(sl):
                        sl[idx-1][1]=sl[idx+1][1]
                        sl.remove(sl[idx+1])
                        sl.remove(sl[idx])
                    elif idx-1 <0 and idx+1>=len(sl):
                        pass
                    elif idx-1<0:
                        sl[idx][1]=sl[idx+1][1]
                        sl.remove(sl[idx+1])
                    else:
                        sl[idx-1][1]=sl[idx][1]
                        sl.remove(sl[idx])
                else:
                    
                    if sl[idx][0]==q[1]:
                        sl[idx][0]+=1
                        if idx ==0:
                            sl.add([0,0])
                        else:
                            sl[idx-1][1]+=1
                    elif sl[idx][1]==q[1]:
                        sl[idx][1]-=1
                        if idx == len(sl)-1:
                            sl.add([len(s)-1,len(s)-1])
                        else:
                            sl[idx+1][0]-=1
                    else:
                        left, right = sl[idx]
                        sl.remove(sl[idx])
                        sl.add([q[1],q[1]])
                        sl.add([left,q[1]-1])
                        sl.add([q[1]+1,right])
            else:
                l = sl.bisect_left([q[1],q[1]])
                if l == len(sl) or sl[l][0]>q[1]: l-=1
                r = sl.bisect_left([q[2],q[2]])
                if r ==len(sl) or sl[r][0]>q[2]: r-=1
                res.append((q[2]-q[1]) - (r-l))

        return res
