# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        step_size = 1
        
        while True:
            prev = dummy
            remaining = prev.next

            num_loops = 0

            while remaining:
                num_loops += 1

                sublists = [None, None]
                sublists_tail = [None, None]

                for i in range(2):
                    sublists[i] = remaining
                    substep_size = step_size

                    while substep_size and remaining:
                        substep_size -= 1
                        sublists_tail[i] = remaining
                        remaining = remaining.next
                
                    if sublists_tail[i]:
                        sublists_tail[i].next = None
        
                while sublists[0] and sublists[1]:
                    if sublists[0].val <= sublists[1].val:
                        prev.next = sublists[0]
                        sublists[0] = sublists[0].next
                    else:
                        prev.next = sublists[1]
                        sublists[1] = sublists[1].next
                    
                    prev = prev.next
                
                if sublists[0]:
                    prev.next = sublists[0]
                    prev = sublists_tail[0]
                
                if sublists[1]:
                    prev.next = sublists[1]
                    prev = sublists_tail[1]
        
            step_size *= 2

            if 1 >= num_loops:
                return dummy.next

        
