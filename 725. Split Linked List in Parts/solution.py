# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        output = []

        curr = head

        while curr:
            curr = curr.next
            length += 1
        
        base_length = length // k
        remainder = length % k

        curr = head

        for i in range(k):
            output.append(curr)

            for j in range(base_length - 1 + (1 if remainder else 0)):
                if not curr:
                    break
                curr = curr.next
            
            remainder -= 1 if remainder > 0 else 0

            if curr:
                curr.next, curr = None, curr.next
        
        return output
