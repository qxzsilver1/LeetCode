class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        res = 0

        n = len(nums)

        count_dict = defaultdict(int)

        for j in range(n - 2, 0, -1):
            count_dict[nums[j + 1] % d] += 1

            for i in range(j):
                res += count_dict[(d - nums[i] - nums[j]) % d]
        
        return res
