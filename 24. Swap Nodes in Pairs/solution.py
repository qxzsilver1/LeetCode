# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        prev = dummy_node
        curr = head

        while curr and curr.next:
            next_pair = curr.next.next
            second_node = curr.next

            second_node.next = curr
            curr.next = next_pair
            prev.next = second_node

            prev = curr
            curr = next_pair
        
        return dummy_node.next
