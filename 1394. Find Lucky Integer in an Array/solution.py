class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)

        res = -1

        for num in cnt:
            if num == cnt[num]:
                res = max(num ,res)
        
        return res
