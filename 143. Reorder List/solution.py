# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        r = slow.next
        prev = slow.next = None

        while r:
            tmp = r.next
            r.next = prev
            prev = r
            r = tmp
        
        l, r = head, prev

        while r:
            tmp_l, tmp_r = l.next, r.next
            l.next = r
            r.next = tmp_l
            l, r = tmp_l, tmp_r
