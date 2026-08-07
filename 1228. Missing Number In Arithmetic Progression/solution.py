class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr_len = len(arr)
        k = (arr[-1] - arr[0]) // (arr_len)

        theo_sum = arr_len * (arr_len + 1) // 2 * k + arr[0] * (arr_len + 1)

        missing_num = theo_sum - sum(arr)

        return missing_num

