class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        l, r = 0, n - 1

        def reverse_list(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse_list(l, r)
        reverse_list(0, k-1)
        reverse_list(k, n - 1)

        return nums
