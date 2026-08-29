class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)

        for i in range(n):
            prev, num = i, arr[i]

            while 0 < num <= n:
                nxt_num = arr[num - 1]
                arr[num - 1] = min(0, arr[num - 1]) - 1

                if num - 1 <= i or num - 1 == prev:
                    break
                prev = num - 1
                num = nxt_num
        
        for i in range(n - 1, -1, -1):
            if -arr[i] == i + 1:
                return i + 1
        
        return -1
