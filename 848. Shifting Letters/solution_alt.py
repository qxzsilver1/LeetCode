class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        res = ''

        shift = sum(shifts) % 26

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')

            res += chr(ord('a') + (idx + shift) % 26)

            shift = (shift - shifts[i]) % 26
        
        return res
