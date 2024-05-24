# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy

        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                tmp = curr.next.next

                while tmp and tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                
                curr.next = tmp.next
            else:
                curr = curr.next
        
        return dummy.next
