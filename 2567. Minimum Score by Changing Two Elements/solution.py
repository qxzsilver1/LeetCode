class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        min1 = min2 = min3 = inf
        max1 = max2 = max3 = -inf

        for x in nums:
            if x < min1:
                min1, min2, min3 = x, min1, min2
            elif x < min2:
                min2, min3 = x, min2
            elif x < min3:
                min3 = x
            
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x
        
        return min(max1 - min3, max2 - min2, max3 - min1)
