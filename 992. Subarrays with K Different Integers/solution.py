class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count_dict = defaultdict(int)
        res = 0

        l_far, l_near = 0, 0

        for r in range(len(nums)):
            count_dict[nums[r]] += 1

            while len(count_dict) > k:
                count_dict[nums[l_near]] -= 1

                if not count_dict[nums[l_near]]:
                    count_dict.pop(nums[l_near])
                
                l_near += 1
                l_far = l_near
            
            while count_dict[nums[l_near]] > 1:
                count_dict[nums[l_near]] -= 1
                l_near += 1

            if len(count_dict) == k:
                res += l_near - l_far + 1

        return res
