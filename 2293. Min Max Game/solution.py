class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)

        while n > 1:

            for i in range(0, n, 2):
                a, b = nums[i], nums[i+1]
                d = i // 2

                if not d % 2:
                    nums[d] = min(a, b)
                else:
                    nums[d] = max(a, b)

            n //= 2
        
        return nums[0]

