# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = ListNode()
        if not head:
            return False
        while head.next:
            if head.val == float("inf"):
                return True
            head.val = float("inf")
            head = head.next
        return False