class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        res = 0

        nums = [x % d for x in nums]

        for i, n in enumerate(nums):
            count_dict = defaultdict(int)

            for m in nums[i + 1:]:
                if -n - m in count_dict:
                    res += count_dict[-n - m]
                
                if d - n - m in count_dict:
                    res += count_dict[d - n - m]
                
                if 2*d - n - m in count_dict:
                    res += count_dict[2*d - n - m]
                
                count_dict[m] += 1
        
        return res
