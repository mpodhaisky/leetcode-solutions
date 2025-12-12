class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x: (int(x[1]), x[0]=="MESSAGE"))
        mentions = [0]*numberOfUsers
        online = set(range(numberOfUsers))
        offline = deque()
        for op, time, s in events:
            time=int(time)
            while offline and offline[0][0]<=time:
                online.add(offline.popleft()[1])
            if op =="OFFLINE":
                online.remove(int(s))
                offline.append((time+60,int(s)))
            else:
                if s=="ALL":
                    for n in range(numberOfUsers):
                        mentions[n]+=1
                elif s=="HERE":
                    for n in online:
                        mentions[n]+=1
                else:
                    for w in s.split():
                        mentions[int(w[2:])]+=1
        return mentions