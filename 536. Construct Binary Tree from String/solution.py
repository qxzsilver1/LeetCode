# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        stack = []
        root = None
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
            elif s[i] == ')':
                stack.pop()
                i += 1
            else:
                j = i

                if s[i] == '-':
                    i += 1
                
                while i < len(s) and s[i].isdigit():
                    i += 1
                
                node = TreeNode(int(s[j:i]))

                if stack:
                    if stack[-1].left is None:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                else:
                    root = node
                stack.append(node)
        
        return root
