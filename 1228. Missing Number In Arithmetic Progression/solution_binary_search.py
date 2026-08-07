class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)

        diff = (arr[-1] - arr[0]) // n

        l, r = 0, n-1

        while l < r:
            m = (l + r) // 2

            if arr[m] == arr[0] + m * diff:
                l = m + 1
            else:
                r = m
        
        return arr[0] + diff * l
