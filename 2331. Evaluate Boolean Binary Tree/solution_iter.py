# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]

        node_value_map = {}

        while stack:
            node = stack.pop()

            if not node.left:
                node_value_map[node] = node.val == 1
            else:
                if node.left in node_value_map and node.right in node_value_map:
                    if node.val == 2:
                        node_value_map[node] = node_value_map[node.left] or node_value_map[node.right]
                    
                    if node.val == 3:
                        node_value_map[node] = node_value_map[node.left] and node_value_map[node.right]
                else:
                    stack.extend([node, node.left, node.right])

        return node_value_map[root]
