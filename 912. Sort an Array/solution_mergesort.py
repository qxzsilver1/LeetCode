class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, left, mid, right):
            arr_left, arr_right = arr[left:mid+1], arr[mid+1:right+1]

            i, j, k = left, 0, 0

            while j < len(arr_left) and k < len(arr_right):
                if arr_left[j] <= arr_right[k]:
                    arr[i] = arr_left[j]
                    j += 1
                else:
                    arr[i] = arr_right[k]
                    k += 1
                
                i += 1
            
            while j < len(arr_left):
                arr[i] = arr_left[j]
                j += 1
                i += 1
            
            while k < len(arr_right):
                arr[i] = arr_right[k]
                k += 1
                i += 1

        def mergeSort(arr, l: int, r: int):
            if l == r:
                return arr
            
            m = l + (r - l) // 2

            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)


            merge(arr, l, m, r)

            return arr
        
        mergeSort(nums, 0, len(nums) - 1)

        return nums
