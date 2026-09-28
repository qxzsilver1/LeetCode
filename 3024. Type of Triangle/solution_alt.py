class Solution:
    def triangleType(self, nums: List[int]) -> str:
        is_triangle = nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]

        nums_set = set(nums)
        n = len(nums_set)

        if n == 1:
            return 'equilateral'
        elif n == 2 and is_triangle:
            return 'isosceles'
        elif n == 3 and is_triangle:
            return 'scalene'
        else:
            return 'none'
