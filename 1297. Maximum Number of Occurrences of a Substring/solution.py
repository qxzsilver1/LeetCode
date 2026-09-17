class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(int)

        res = 0

        l = 0

        unique_chars = defaultdict(int)

        for r in range(len(s)):
            unique_chars[s[r]] += 1

            while len(unique_chars) > maxLetters or r - l + 1 > minSize:
                unique_chars[s[l]] -= 1

                if unique_chars[s[l]] == 0:
                    del unique_chars[s[l]]
                l += 1
            
            curr_str = s[l:r + 1]

            if r - l + 1 == minSize and len(unique_chars) <= maxLetters:
                counts[curr_str] += 1

                res = max(res, counts[curr_str])
            
        return res
