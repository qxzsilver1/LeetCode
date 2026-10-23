# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        wanted = {node.val for node in nodes}
        order = [root]
        
        for node in order:
            if node.left: order.append(node.left)
            if node.right: order.append(node.right)
        
        counts = {}
        
        for node in reversed(order):
            count = int(node.val in wanted)
            if node.left: count += counts[node.left.val]
            if node.right: count += counts[node.right.val]
            if count == len(nodes): return node
            counts[node.val] = count
        return root
