# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr_node = head
        last_m_node = head

        while curr_node:
            m_count, n_count = m, n

            while curr_node and m_count != 0:
                last_m_node = curr_node
                curr_node = curr_node.next
                m_count -= 1
            
            while curr_node and n_count != 0:
                curr_node = curr_node.next
                n_count -= 1
            
            last_m_node.next = curr_node

        return head
