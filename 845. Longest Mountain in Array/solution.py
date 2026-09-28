class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)

        res = 0
        base = 0

        while base < n:
            r = base

            if r + 1 < n and arr[r] < arr[r + 1]:
                while r + 1 < n and arr[r] < arr[r + 1]:
                    r += 1
                
                if r + 1 < n and arr[r] > arr[r + 1]:
                    while r + 1 < n and arr[r] > arr[r + 1]:
                        r += 1
                    
                    res = max(res, r - base + 1)
            
            base = max(r, base + 1)
        
        return res
