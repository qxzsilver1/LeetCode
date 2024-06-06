class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        x, y = 0, 0

        for i in range(1, n+1):
            x += nums[i - 1] - i
            y += nums[i - 1] ** 2 - i ** 2

        missing = (y - x ** 2) // (2 * x)
        duplicate = missing + x

        return [duplicate, missing]
