class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        res = 0
        m = len(nums)
        
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            return
        
        def partition(arr, l, r, val):
            i = 0
            for i in range(l, r):
                if arr[i] == val:
                    break
            
            swap(arr, i, r)

            pivot_val = arr[r]
            res_idx = l

            for i in range(l, r + 1):
                if arr[i] < pivot_val:
                    swap(arr, res_idx, i)
                    res_idx += 1
            
            swap(arr, r, res_idx)
            return res_idx
        
        def findMedian(arr, l, sub_len):
            arr[l:l + sub_len].sort()

            return arr[l + sub_len // 2]
        
        def kthSmallest(arr, l, r, k):
            if k > 0 and k <= r - l + 1:
                n = r - l + 1
                i = 0

                median_arr = [0] * ((n + 4) // 5)

                for i in range(n // 5):
                    median_arr[i] = findMedian(arr, l + 5 * i, 5)
                
                if 5 * i < n:
                    median_arr[i] = findMedian(arr, l + 5 * i, n % 5)
                    i += 1
                
                median_of_medians = median_arr[i - 1] if (i == 1) else kthSmallest(median_arr, 0, i - 1, i // 2)

                pos = partition(arr, l, r, median_of_medians)

                if pos - l == k - 1:
                    return arr[pos]
                
                if pos - l > k - 1:
                    return kthSmallest(arr, l, pos - 1, k)
                
                return kthSmallest(arr, pos + 1, r, k - pos + l - 1)
            
            return float('inf')
        
        median = kthSmallest(nums, 0, m - 1, m // 2 + 1)

        for num in nums:
            res += abs(median - num)
        
        return res
