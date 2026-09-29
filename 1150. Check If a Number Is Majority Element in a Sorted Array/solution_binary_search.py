class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        def lowerBound() -> int:
            """
            Returns the index of the first element equal to or greater than the target.
            If there is no instance of the target in the list, it returns the length of the list.
            """
            start = 0
            end = len(nums) - 1
            index = len(nums)

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] >= target:
                    end = mid - 1
                    index = mid
                else:
                    start = mid + 1

            return index
        
        def upperBound() -> int:
            """
            Returns the index of the first element greater than the target.
            If there is no instance of the target in the list, it returns the length of the list.
            """
            start = 0
            end = len(nums) - 1
            index = len(nums)

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                    index = mid
                else:
                    start = mid + 1

            return index
        
        first_index = lowerBound()
        next_to_last_index = upperBound()
        
        return next_to_last_index - first_index > len(nums) // 2
