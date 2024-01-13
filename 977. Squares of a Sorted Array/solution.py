class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []

        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                output.append(nums[l] ** 2)
                l += 1
            else:
                output.append(nums[r] ** 2)
                r -= 1
        
        return output[::-1]
