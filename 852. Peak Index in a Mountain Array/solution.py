class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr) - 2 # peak is not at the edges

        while l <= r:
            m = l + (r - l) // 2

            if arr[m-1] < arr[m] < arr[m+1]:
                l = m + 1
            elif arr[m-1] > arr[m] > arr[m+1]:
                r = m - 1
            else:
                break

        return m
