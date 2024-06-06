class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]

        cnt = Counter(nums)

        for i in range(1, len(nums) + 1):
            if cnt[i] == 0:
                res[1] = i
            
            if cnt[i] == 2:
                res[0] = i
        
        return res
