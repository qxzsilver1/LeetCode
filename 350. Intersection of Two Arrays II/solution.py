class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_cnt = Counter(nums1)

        res = []

        for num in nums2:
            if num in nums1_cnt and nums1_cnt[num] != 0:
                res.append(num)
                nums1_cnt[num] -= 1
        
        return res
