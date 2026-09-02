class Solution:
    def averageValue(self, nums: List[int]) -> int:
        curr_sum = 0
        curr_cnt = 0

        for num in nums:
            if num % 6 == 0:
                curr_sum += num
                curr_cnt += 1
        
        return curr_sum // curr_cnt if curr_cnt else 0
