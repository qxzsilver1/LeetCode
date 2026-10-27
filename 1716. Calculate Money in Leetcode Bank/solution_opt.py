class Solution:
    def totalMoney(self, n: int) -> int:
        SUM = lambda x: (x * (x + 1)) >> 1
        weeks = n // 7
        res = SUM(weeks - 1) * 7 + weeks * SUM(7)
        res += SUM(n % 7) + weeks * (n % 7)
        return res
