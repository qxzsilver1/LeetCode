class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''

        nums = list(range(1, n + 1))

        for i in range(n, 0, -1):
            digit = (k - 1) // factorial(i - 1)
            k -= digit * factorial(i - 1)

            res += str(nums[digit])

            nums.remove(nums[digit])
        
        return res
