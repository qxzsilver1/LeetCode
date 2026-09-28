class Solution:
    def maxDepth(self, s: str) -> int:
        res, stack = 0, []

        for c in s:
            if c == "(":
                stack.append(c)
                res = max(res, len(stack))
            elif c == ")":
                stack.pop()

        return res
