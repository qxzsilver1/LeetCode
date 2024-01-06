# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_res = ListNode()
        curr_node = l_res
        
        total = 0
        carry = 0
        
        while (l1 != None) or (l2 != None) or (total > 0):
            if (l1 != None):
                total += l1.val
                l1 = l1.next
            
            if (l2 != None):
                total += l2.val
                l2 = l2.next
            
            carry = total // 10
            total = total % 10
            
            curr_node.next = ListNode(total)
            curr_node = curr_node.next
            
            total = carry
            carry = 0
        
        return l_res.next
