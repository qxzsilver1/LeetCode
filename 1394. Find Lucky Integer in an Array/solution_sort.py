class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        streak = 0
        for i in range(len(arr) - 1, -1, -1):
            streak += 1
            if i == 0 or (arr[i] != arr[i - 1]):
                if arr[i] == streak:
                    return arr[i]
                streak = 0
        return -1
