class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0

        def dfs(i):
            nonlocal res
            if i == len(s):
                return 0

            cur = dfs(i + 1)
            
            if s[i] == '(':
                cur += 1
            elif s[i] == ')':
                cur -= 1

            res = max(res, abs(cur))
            
            return cur

        dfs(0)
        return res
