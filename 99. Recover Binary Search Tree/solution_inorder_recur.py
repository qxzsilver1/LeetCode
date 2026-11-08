# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            arr.append(node)
            inorder(node.right)

        inorder(root)
        node1, node2 = None, None

        for i in range(len(arr) - 1):
            if arr[i].val > arr[i + 1].val:
                node2 = arr[i + 1]
                if node1 is None:
                    node1 = arr[i]
                else:
                    break
        node1.val, node2.val = node2.val, node1.val
