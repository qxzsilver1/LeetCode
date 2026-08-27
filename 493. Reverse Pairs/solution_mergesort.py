class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge(arr, start, mid, end):
            n1, n2 = mid - start + 1, end - mid

            left = [0] * n1
            right = [0] * n2

            for i in range(n1):
                left[i] = arr[start + i]
            
            for j in range(n2):
                right[j] = arr[mid + 1 + j]
            
            i, j = 0, 0

            for k in range(start, end + 1):
                if j >= n2 or i < n1 and left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
        
        def mergesortCount(arr, start, end):
            if start < end:
                mid = (start + end) // 2

                cnt = mergesortCount(arr, start, mid) + mergesortCount(arr, mid + 1, end)

                j = mid + 1

                for i in range(start, mid + 1):
                    while j <= end and arr[i] > 2 * arr[j]:
                        j += 1
                    
                    cnt += j - (mid + 1)
                
                merge(arr, start, mid, end)

                return cnt
            else:
                return 0
        
        return mergesortCount(nums, 0, len(nums) - 1)
