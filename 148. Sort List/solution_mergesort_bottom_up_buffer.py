# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        buffer_size = 8

        dummy = ListNode(0)
        dummy.next = head

        step_size = 1
        
        while True:
            prev = dummy
            remaining = prev.next

            num_loops = 0

            while remaining:
                num_loops += 1

                sublists = [None] * buffer_size
                sublists_tail = [None] * buffer_size

                for i in range(buffer_size):
                    sublists[i] = remaining
                    substep_size = step_size

                    while substep_size and remaining:
                        substep_size -= 1
                        sublists_tail[i] = remaining
                        remaining = remaining.next
                
                    if sublists_tail[i]:
                        sublists_tail[i].next = None
        
                num_sublists = buffer_size

                while 1 < num_sublists:
                    sub_dummy = ListNode()

                    for i in range(0, num_sublists, 2):
                        sub_prev = sub_dummy
                        sub_prev.next = None

                        while sublists[i] and sublists[i+1]:
                            if sublists[i].val <= sublists[i+1].val:
                                sub_prev.next = sublists[i]
                                sublists[i] = sublists[i].next
                            else:
                                sub_prev.next = sublists[i+1]
                                sublists[i+1] = sublists[i+1].next
                            
                            sub_prev = sub_prev.next
                    
                        if sublists[i]:
                            sub_prev.next = sublists[i]
                            sublists_tail[i // 2] = sublists_tail[i]
                        
                        if sublists[i+1]:
                            sub_prev.next = sublists[i+1]
                            sublists_tail[i // 2] = sublists_tail[i+1]
                        
                        sublists[i // 2] = sub_dummy.next
                    
                    num_sublists //= 2
                
                prev.next = sublists[0]
                prev = sublists_tail[0]
        
            step_size *= buffer_size

            if 1 >= num_loops:
                return dummy.next

        
