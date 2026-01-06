# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.length= 0
        dummy = head
        while head:
            self.length+=1
            head = head.next
        self.head = dummy
        

    def getRandom(self) -> int:
        idx = randint(0,self.length-1)
        dummy = self.head
        for _ in range(idx):
            dummy=dummy.next
        return dummy.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()