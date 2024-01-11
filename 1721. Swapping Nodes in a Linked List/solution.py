# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for i in range(k-1):
            curr = curr.next
        
        l = curr
        r = head

        while curr.next:
            curr = curr.next
            r = r.next
        
        l.val, r.val = r.val, l.val

        return head
