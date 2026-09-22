class Solution:
    def integerBreak(self, n: int) -> int:
        def dfs(num, i):
            if min(num, i) == 0:
                return 1

            if i > num:
                return dfs(num, num)

            return max(i * dfs(num - i, i), dfs(num, i - 1))

        return dfs(n, n - 1)
