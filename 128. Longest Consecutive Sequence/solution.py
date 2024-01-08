class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest_seq_len = 0

        for n in nums:
            if (n - 1) not in setNums:
                length = 0

                while (n + length) in setNums:
                    length += 1
                longest_seq_len = max(length, longest_seq_len)
        
        return longest_seq_len
