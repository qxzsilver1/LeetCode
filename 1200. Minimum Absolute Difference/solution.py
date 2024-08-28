class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = 10 ** 6
        min_diff_arr = []

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < min_diff:
                min_diff = arr[i] - arr[i-1]
                min_diff_arr = [[arr[i-1], arr[i]]]
            elif arr[i] - arr[i-1] == min_diff:
                min_diff_arr.append([arr[i-1], arr[i]])
        
        return min_diff_arr
