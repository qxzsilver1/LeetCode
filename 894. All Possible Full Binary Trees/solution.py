# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2:
            return []

        dp = { 0: [], 1: [TreeNode()] }
        
        def backtrack(n):
            if n in dp:
                return dp[n]
            
            res = []

            for l in range(n):
                r = n - 1 - l

                if not l % 2 or not r % 2:
                    continue
                
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for l_tree in leftTrees:
                    for r_tree in rightTrees:
                        res.append(TreeNode(0, l_tree, r_tree))
            dp[n] = res

            return dp[n]
        
        return backtrack(n)
