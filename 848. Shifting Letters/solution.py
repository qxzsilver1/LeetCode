class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(shifts)
        suffix_sum = [0] * n
        suffix_sum[n - 1] = shifts[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = shifts[i] + suffix_sum[i + 1]

        res = ''

        for i in range(n):
            shift = suffix_sum[i] % 26

            shifted_char = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
            res += shifted_char
        
        return res
