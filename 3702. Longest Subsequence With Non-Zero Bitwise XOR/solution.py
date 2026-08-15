class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        curr_xor = 0

        is_all_zeros = True

        for a in nums:
            curr_xor ^= a

            if a > 0:
                is_all_zeros = False
        
        if curr_xor > 0:
            return n
        
        return n-1 if is_all_zeros == False else 0
