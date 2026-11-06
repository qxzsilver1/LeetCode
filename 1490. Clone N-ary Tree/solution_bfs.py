"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        node_copy = Node(root.val)
        q = deque([(root, node_copy)])

        while q:
            old_node, new_node = q.popleft()

            for child in old_node.children:
                new_child_node = Node(child.val)

                new_node.children.append(new_child_node)

                q.append((child, new_child_node))
        
        return node_copy
