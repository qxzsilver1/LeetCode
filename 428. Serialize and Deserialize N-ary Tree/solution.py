"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return []
        
        q = deque([root])
        res = [root.val]

        while q:
            node = q.popleft()

            if not node:
                continue
            
            for child in node.children:
                q.append(child)
            
            res.append(len(node.children))
            res.extend([child.val for child in node.children])
        
        return res
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        root = Node(data[0])
        data = deque(data[1:])

        q = deque([root])

        while q:
            node = q.popleft()

            if not node:
                continue
            
            for _ in range(data.popleft()):
                child = Node(data.popleft())
                node.children.append(child)
                q.append(child)
            
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
