class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = nums1[0]

        has_odd = False

        for num in nums1:
            if num < min_val:
                min_val = num
            
            if num & 1:
                has_odd = True
        
        if min_val & 1:
            return True
        
        return not has_odd
