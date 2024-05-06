# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mono_stack = []
        curr = head

        while curr:
            while mono_stack and curr.val > mono_stack[-1]:
                mono_stack.pop()
            mono_stack.append(curr.val)
            curr = curr.next
        
        dummy = ListNode()
        curr = dummy

        for n in mono_stack:
            curr.next = ListNode(n)
            curr = curr.next
        
        return dummy.next
