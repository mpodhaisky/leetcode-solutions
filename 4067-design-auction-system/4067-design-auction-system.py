class AuctionSystem:

    def __init__(self):
        self.id2usr = defaultdict(SortedList)
        self.usrItem2bid = {}
    def addBid(self, usrId: int, itemId: int, bidAmount: int) -> None:
        try:
            self.id2usr[itemId].remove([self.usrItem2bid[(usrId,itemId)],usrId])
        except:
            pass
        self.usrItem2bid[(usrId,itemId)]=bidAmount
        self.id2usr[itemId].add([bidAmount,usrId])

    def updateBid(self, usrId: int, itemId: int, bidAmount: int) -> None:
        self.id2usr[itemId].remove([self.usrItem2bid[(usrId,itemId)],usrId])
        self.usrItem2bid[(usrId,itemId)]=bidAmount
        self.id2usr[itemId].add([bidAmount,usrId])
        

    def removeBid(self, usrId: int, itemId: int) -> None:
        self.id2usr[itemId].remove([self.usrItem2bid[(usrId,itemId)],usrId])
        

    def getHighestBidder(self, itemId: int) -> int:
        try:
            return self.id2usr[itemId][-1][-1]
        except:
            return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)