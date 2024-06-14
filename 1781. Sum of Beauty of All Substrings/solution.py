class Solution:
    def beautySum(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            freq_counter = [0] * 26

            for j in range(i, len(s)):
                freq_counter[ord(s[j]) - ord('a')] += 1

                res += max(freq_counter) - min(x for x in freq_counter if x)
        
        return res
