class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_val = max(nums)

        for divisor in range(1, max_val + 1):
            sum_res = 0
            over_threshold = True

            for num in nums:
                sum_res += ceil((num * 1.0) / divisor)

                if sum_res > threshold:
                    over_threshold = False
                    break
            
            if over_threshold:
                return divisor
        
        return -1
