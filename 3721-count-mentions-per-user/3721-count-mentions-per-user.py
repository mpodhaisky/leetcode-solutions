class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        filtered=[]
        mentions=[0]*numberOfUsers
        allcnt=0
        for a,b ,text in events:
            if text =="ALL":
                allcnt+=1
            elif text.startswith("id"):
                for w in text.split():
                        mentions[int(w[2:])]+=1
            else:
                filtered.append([a,b,text])
            if text=="HERE":
                allcnt+=1
        for i in range(numberOfUsers):
            mentions[i]+=allcnt

        filtered.sort(key = lambda x: (int(x[1]), x[0]=="MESSAGE"))
        
        mono = deque()
        cnt=0
        for op, time, s in filtered + [["MESSAGE","1000000","HERE"]]:
            time=int(time)
            while mono and mono[0][0]+60<=time:
                if mono[0][1]!=-1:
                    mentions[mono[0][1]]-=cnt
                else:
                    cnt-=1
                mono.popleft()
            if op =="OFFLINE":
                mono.append((time,int(s)))
            else:
                cnt+=1
                mono.append((time,-1))
        return mentions