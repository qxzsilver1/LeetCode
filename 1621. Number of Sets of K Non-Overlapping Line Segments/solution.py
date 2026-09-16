class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        M = 10 ** 9 + 7
        return math.comb(n + k - 1, 2 * k) % M
