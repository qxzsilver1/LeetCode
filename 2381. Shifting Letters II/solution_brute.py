class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        s = [ord(c) - ord('a') for c in s]

        for l, r, d in shifts:
            for i in range(l, r + 1):
                s[i] += 1 if d else -1
                s[i] %= 26
        
        s = [chr(num + ord('a')) for num in s]

        return ''.join(s)
