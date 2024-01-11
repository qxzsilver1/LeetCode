# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev, curr = head, head.next

        while curr:
            nxt = curr.next

            if prev.val == curr.val:
                prev.next = nxt
            else:
                prev = curr
            
            curr = nxt
        
        return head
