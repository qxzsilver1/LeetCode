class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        max_idx = -1
        n = len(arr)
        output = []

        def max_index(arr):
            return max(enumerate(arr), key = lambda x: x[1])[0]
        
        def flip(arr, k):
            l, r = 0, k

            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        while n > 1:
            max_idx = max_index(arr[:n])

            if max_idx != n:
                flip(arr, max_idx)
                flip(arr, n-1)
                output.append(max_idx + 1)
                output.append(n)
            
            n -= 1
        
        return output
