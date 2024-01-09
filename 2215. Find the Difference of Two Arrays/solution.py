class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        output1, output2 = set(), set()

        for n in nums1:
            if n not in nums2_set:
                output1.add(n)

        for n in nums2:
            if n not in nums1_set:
                output2.add(n)

        return [list(output1), list(output2)]
