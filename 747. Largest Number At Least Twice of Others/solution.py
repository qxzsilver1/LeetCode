class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, largest_idx = -1, -1
        second_largest = -1

        for i, n in enumerate(nums):
            if n > largest:
                second_largest = largest
                largest, largest_idx = n, i
            elif n > second_largest:
                second_largest = n
        
        return largest_idx if largest >= 2 * second_largest else -1
