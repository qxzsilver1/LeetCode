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
        def isBST(node):
            if not node:
                return True

            q = deque([(node, float("-inf"), float("inf"))])
            while q:
                cur, left, right = q.popleft()
                if not (left < cur.val < right):
                    return False
                if cur.left:
                    q.append((cur.left, left, cur.val))
                if cur.right:
                    q.append((cur.right, cur.val, right))

            return True

        def dfs1(node1, node2):
            if not node2 or node1 == node2:
                return False

            node1.val, node2.val = node2.val, node1.val
            if isBST(root):
                return True

            node1.val, node2.val = node2.val, node1.val
            return dfs1(node1, node2.left) or dfs1(node1, node2.right)


        def dfs(node):
            if not node:
                return False

            if dfs1(node, root):
                return True

            return dfs(node.left) or dfs(node.right)

        dfs(root)
        return root
