class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        negative_counts = [0] * 50
        res = [0] * (len(nums) - k + 1)

        for i in range(len(nums)):
            if nums[i] < 0:
                negative_counts[nums[i] + 50] += 1
            
            if i - k >= 0 and nums[i-k] < 0:
                negative_counts[nums[i-k] + 50] -= 1
            
            if i - k + 1 < 0:
                continue
            
            cnt = 0

            for j in range(50):
                cnt += negative_counts[j]

                if cnt >= x:
                    res[i - k + 1] = j - 50
                    break
        
        return res
