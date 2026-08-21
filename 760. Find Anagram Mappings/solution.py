class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_pos = {}

        for i in range(len(nums2)):
            num_to_pos[nums2[i]] = i
        
        mapping = [0] * len(nums1)

        for i in range(len(nums1)):
            mapping[i] = num_to_pos[nums1[i]]
        
        return mapping
