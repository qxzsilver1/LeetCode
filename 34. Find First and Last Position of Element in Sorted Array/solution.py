class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)

        return [left, right]
    
    def binarySearch(self, arr: List[int], target: int, left_bias: bool):
        l, r = 0, len(arr) - 1
        i = -1

        while l <= r:
            m = l + (r - l) // 2

            if target > arr[m]:
                l = m + 1
            elif target < arr[m]:
                r = m - 1
            else:
                i = m

                if left_bias:
                    r = m - 1
                else:
                    l = m + 1
        
        return i
