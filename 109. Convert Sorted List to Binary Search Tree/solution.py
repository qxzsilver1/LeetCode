# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        root = head

        list_size = 0

        while root:
            root = root.next
            list_size += 1
        
        def convertToBST(l, r):
            nonlocal head

            if l > r:
                return None
            
            m = (l + r) // 2

            left = convertToBST(l, m - 1)
            
            node = TreeNode(head.val)
            node.left = left

            head = head.next

            node.right = convertToBST(m + 1, r)
            
            return node
        
        return convertToBST(0, list_size - 1)
