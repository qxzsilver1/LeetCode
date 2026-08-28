class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)

        arr = [[v, i] for i, v in enumerate(nums)]

        res = [0] * n

        def merge(arr, left, right, mid):
            i = left
            j = mid
            tmp = []

            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    res[arr[i][1]] += j - mid
                    tmp.append(arr[i])
                    i += 1
                else:
                    tmp.append(arr[j])
                    j += 1
            
            while i < mid:
                res[arr[i][1]] += j - mid
                tmp.append(arr[i])
                i += 1
            
            while j < right:
                tmp.append(arr[j])
                j += 1
            
            for i in range(left, right):
                arr[i] = tmp[i - left]

        def mergesort(arr, left, right):
            if right - left <= 1:
                return
            
            mid = (left + right) // 2
            
            mergesort(arr, left, mid)
            mergesort(arr, mid, right)
            merge(arr, left, right, mid)
        
        mergesort(arr, 0, n)

        return res
