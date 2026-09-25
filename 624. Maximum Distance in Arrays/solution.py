class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        res = 0

        curr_min, curr_max = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(res, max(arr[-1] - curr_min, curr_max - arr[0]))
            curr_min = min(curr_min, arr[0])
            curr_max = max(curr_max, arr[-1])
        
        return res
