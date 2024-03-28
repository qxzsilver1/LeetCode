class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        
        l = 0
        curr_sum, res = 0, 0

        for r in range(len(s)):
            curr_sum += 1 if s[r] in vowel_set else 0

            if r - l + 1 > k:
                curr_sum -= 1 if s[l] in vowel_set else 0
                l += 1
            
            res = max(res, curr_sum)
        
        return res
