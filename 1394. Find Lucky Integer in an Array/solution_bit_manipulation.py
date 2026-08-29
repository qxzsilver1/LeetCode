class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for num in arr:
            idx = num & ((1 << 10) - 1)

            if idx <= len(arr):
                arr[idx - 1] += (1 << 10)
        
        for i in range(len(arr) - 1, -1, -1):
            cnt = arr[i] >> 10

            if cnt == i + 1:
                return i + 1
        
        return -1
