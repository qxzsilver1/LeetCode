class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        pref_sum_to_idx = {0 : -1}

        curr_sum = 0
        res = n + 1
        min_length = n

        for i, x in enumerate(arr):
            curr_sum += x

            if curr_sum - target in pref_sum_to_idx:
                j = pref_sum_to_idx[curr_sum - target]
                curr_length = i - j

                res = min(res, curr_length + (n if j == -1 else arr[j]))
                min_length = min(min_length, curr_length)
            
            arr[i] = min_length
            pref_sum_to_idx[curr_sum] = i
        
        return -1 if res == n + 1 else res
