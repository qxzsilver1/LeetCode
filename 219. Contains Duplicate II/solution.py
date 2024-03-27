class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sliding_window_set = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                sliding_window_set.remove(nums[l])
                l += 1
            
            if nums[r] in sliding_window_set:
                return True
            
            sliding_window_set.add(nums[r])
        
        return False
