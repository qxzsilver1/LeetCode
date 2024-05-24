# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        curr = dummy

        count_dict = Counter()

        while curr.next:
            count_dict[curr.next.val] += 1
            curr = curr.next
        
        curr = dummy

        while curr.next:
            if count_dict[curr.next.val] >= 2:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
