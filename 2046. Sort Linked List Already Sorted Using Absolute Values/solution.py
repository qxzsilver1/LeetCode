# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: ListNode | None) -> ListNode | None:
        negative = None

        dummy = ListNode(0)
        tail = dummy

        while head:
            following = head.next

            if head.val < 0:
                head.next = negative
                negative = head
            else:
                tail.next = head
                tail = head
                tail.next = None
            head = following
        
        if negative is None:
            return dummy.next
        
        tail = negative

        while tail.next:
            tail = tail.next
        
        tail.next = dummy.next

        return negative
