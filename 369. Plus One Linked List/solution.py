# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel_node = ListNode(0)
        sentinel_node.next = head

        not_nine = sentinel_node

        while head:
            if head.val != 9:
                not_nine = head
            head = head.next
        
        not_nine.val += 1
        not_nine = not_nine.next

        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        
        return sentinel_node if sentinel_node.val else sentinel_node.next
