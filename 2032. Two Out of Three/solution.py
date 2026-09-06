class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count_dict = defaultdict(int)

        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)

        res_set = set()

        for s in [nums1, nums2, nums3]:
            for num in s:
                count_dict[num] += 1

                if count_dict[num] >= 2:
                    res_set.add(num)
        
        return list(res_set)
