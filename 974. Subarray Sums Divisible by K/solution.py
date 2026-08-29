class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_mod = 0

        mod_groups = [0] * k
        mod_groups[0] = 1
        
        res = 0

        for num in nums:
            prefix_mod = (prefix_mod + num % k + k) % k

            res += mod_groups[prefix_mod]
            mod_groups[prefix_mod] += 1
        
        return  res
