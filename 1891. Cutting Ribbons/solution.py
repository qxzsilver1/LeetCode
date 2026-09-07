class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 0, max(ribbons)

        def isPossible(x: int, ribbons: list[int], k: int) -> bool:
            total_ribbons = 0
            for ribbon in ribbons:
                total_ribbons += ribbon // x

                if total_ribbons >= k:
                    return True
            return False

        while l < r:
            m = (l + r + 1) // 2

            if isPossible(m, ribbons, k):
                l = m
            else:
                r = m - 1
        
        return l
