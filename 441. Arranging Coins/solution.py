class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n

        res = 0

        while l <= r:
            m = l + (r - l) // 2
            coins = m / 2 * (m + 1)

            if coins > n:
                r = m - 1
            else:
                l = m + 1
                res = max(res, m)
        
        return res
