class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num_negatives = 0

        for n in nums:
            if n == 0:
                return 0
            
            if n < 0:
                num_negatives += 1

        return -1 if num_negatives % 2 else 1
