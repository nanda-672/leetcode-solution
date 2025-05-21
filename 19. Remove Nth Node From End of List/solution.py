# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        lp = rp = dummy

        for i in range(n+1):
            rp = rp.next
        
        while rp:
            rp = rp.next
            lp = lp.next
        
        lp.next = lp.next.next

        return dummy.next