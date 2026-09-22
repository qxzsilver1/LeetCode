class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(num, i):
            if min(num, i) == 0:
                return 1
            if (num, i) in dp:
                return dp[(num, i)]
            if i > num:
                dp[(num, i)] = dfs(num, num)
                return dp[(num, i)]

            dp[(num, i)] = max(i * dfs(num - i, i), dfs(num, i - 1))
            return dp[(num, i)]

        return dfs(n, n - 1)
