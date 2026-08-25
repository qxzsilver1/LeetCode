# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        stack = []
        curr = root
        visited = None

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]

            if curr.right and curr.right != visited:
                curr = curr.right
                continue

            stack.pop()

            if not curr.left and not curr.right and curr.val == target:
                if not stack:
                    return None

                parent = stack[-1]

                if parent.left == curr:
                    parent.left = None
                elif parent.right == curr:
                    parent.right = None
            
            else:
                visited = curr

            curr = None

        return root
