"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        
        def dfs(node, siblings):
            if not node:
                return None
            
            t_node = TreeNode(node.val)
            t_node.right = dfs(next(siblings, None), siblings)

            children = iter(node.children)
            t_node.left = dfs(next(children, None), children)

            return t_node
        
        return dfs(root, iter(()))
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':

        def traverse(t_node, parent):
            if not t_node:
                return None
            
            node = Node(t_node.val, [])

            if t_node.left:
                node.children.append(traverse(t_node.left, node))
            
            if t_node.right:
                parent.children.append(traverse(t_node.right, parent))
            
            node.children = node.children[::-1]

            return node
        return traverse(data, None)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
