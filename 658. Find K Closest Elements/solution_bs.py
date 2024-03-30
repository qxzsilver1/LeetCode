class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        val, idx = arr[0], 0

        while l <= r:
            m = l + (r - l) // 2

            curr_diff = abs(arr[m] - x)
            res_diff = abs(val - x)

            if curr_diff < res_diff or (curr_diff == res_diff and arr[m] < val):
                val, idx = arr[m], m

            if arr[m] > x:
                r = m - 1
            elif arr[m] < x:
                l = m + 1
            else:
                break
        
        l = r = idx

        for i in range(k-1):
            if l == 0:
                r += 1
            elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
                l -= 1
            else:
                r += 1
        
        return arr[l:r+1]
        
