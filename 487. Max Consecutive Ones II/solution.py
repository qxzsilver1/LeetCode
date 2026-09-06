class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_seq = 0

        l, r = 0, 0

        num_zeroes = 0

        while r < len(nums):
            if nums[r] == 0:
                num_zeroes += 1
            
            while num_zeroes == 2:
                if nums[l] == 0:
                    num_zeroes -= 1
                l += 1
            
            longest_seq = max(longest_seq, r - l + 1)

            r += 1
        
        return longest_seq
