# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append('n')
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        self.i = 0

        def dfs():
            if values[self.i] == 'n':
                self.i += 1
                return None
            
            node = TreeNode(int(values[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
