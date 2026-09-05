class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def recur(max1, max2, max3, char1, char2, char3):
            if max1 < max2:
                return recur(max2, max1, max3, char2, char1, char3)
            if max2 < max3:
                return recur(max1, max3, max2, char1, char3, char2)
            if max2 == 0:
                return [char1] * min(2, max1)

            use1 = min(2, max1)
            use2 = 1 if max1 - use1 >= max2 else 0
            res = [char1] * use1 + [char2] * use2
            return res + recur(max1 - use1, max2 - use2, max3, char1, char2, char3)

        return ''.join(recur(a, b, c, 'a', 'b', 'c'))
