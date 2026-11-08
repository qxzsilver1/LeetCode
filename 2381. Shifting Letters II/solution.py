class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)

        for l, r, diff in shifts:
            prefix_diff[r + 1] += 1 if diff else -1
            prefix_diff[l] += -1 if diff else 1
        
        diff = 0

        res = [ord(c) - ord('a') for c in s]

        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            res[i - 1] = (diff + res[i - 1]) % 26 # or (diff + res[i - 1] + 26) % 26 in other languages
        
        s = [chr(ord('a') + n) for n in res]

        return ''.join(s)
