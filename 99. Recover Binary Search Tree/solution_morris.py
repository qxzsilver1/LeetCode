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
        node1 = node2 = prev = None
        curr = root

        while curr:
            if not curr.left:
                if prev and prev.val > curr.val:
                    node2 = curr
                    if not node1:
                        node1 = prev
                prev = curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev and prev.val > curr.val:
                        node2 = curr
                        if not node1:
                            node1 = prev
                    prev = curr
                    curr = curr.right

        node1.val, node2.val = node2.val, node1.val
