class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index_dict = { 0 : -1 }
        total = 0

        for i, n in enumerate(nums):
            total += n
            rem = total % k

            if rem not in remainder_index_dict:
                remainder_index_dict[rem] = i
            elif i - remainder_index_dict[rem] > 1:
                return True
        
        return False
