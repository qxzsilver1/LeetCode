class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if  len(nums) < 2:
            return 0
        
        max_val = max(nums)
        exp = 1
        radix = 10
        aux = [0] * len(nums)

        while max_val // exp > 0:
            count = [0] * radix

            for num in nums:
                count[(num // exp) % 10] += 1
            
            for i in range(1, radix):
                count[i] += count[i - 1]
            
            i = len(nums) - 1

            while i >= 0:
                aux[count[(nums[i] // exp) % 10] - 1] = nums[i]
                count[(nums[i] // exp) % 10] -= 1
                i -= 1
            
            for i in range(len(nums)):
                nums[i] = aux[i]
            
            exp *= 10
        
        max_gap = 0

        for i in range(len(nums) - 1):
            max_gap = max(nums[i + 1] - nums[i], max_gap)
        
        return max_gap
