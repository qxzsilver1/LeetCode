class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1

            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum == target:
                    return three_sum
                
                if abs(three_sum - target) < abs(res - target):
                    res = three_sum
                
                if three_sum < target:
                    l += 1
                else:
                    r -= 1
        
        return res
