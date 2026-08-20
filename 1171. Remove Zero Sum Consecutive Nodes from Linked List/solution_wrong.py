# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        st = []

        curr = head
        prev = head
        curr_sum = 0

        while curr.next:
            if curr_sum + curr.val == 0:
                top_val = curr.val
                while top_val != 0:
                    top_val += st.pop().val
                
                curr_sum = 0
                curr = curr.next
                continue
            
            if st and st[-1].val + curr.val == 0:
                val = st.pop().val
                curr_sum -= val
                curr = curr.next
                continue
            
            st.append(curr)
            curr_sum += curr.val
            curr = curr.next
        
        if curr_sum + curr.val == 0:
                top_val = curr.val
                while top_val != 0:
                    top_val += st.pop().val
                
                curr_sum = 0
        elif st and st[-1].val + curr.val == 0:
            val = st.pop().val
            curr_sum -= val
        else:
            st.append(curr)
        
        new_head = st[0] if st else None
        curr_node = new_head

        if len(st) == 1:
            curr_node.next = None
            return new_head

        for node in st[1:]:
            curr_node.next = node
            curr_node = node
        
        return new_head
