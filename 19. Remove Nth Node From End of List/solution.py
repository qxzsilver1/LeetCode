# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        left = dummy_node
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy_node.next
