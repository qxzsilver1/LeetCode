class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = dict()

        for n in nums:
            if n in nums_count:
                return True
            else:
                nums_count[n] = 1

        return False 
