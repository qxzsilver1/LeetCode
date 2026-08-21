class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bits_to_shift = 7

        num_to_get_last_bits = (1 << bits_to_shift) - 1

        for i in range(len(nums1)):
            nums1[i] = (nums1[i] << bits_to_shift) + i
            nums2[i] = (nums2[i] << bits_to_shift) + i
        
        nums1.sort()
        nums2.sort()

        mapping = [0] * len(nums1)

        for i in range(len(nums1)):
            mapping[nums1[i] & num_to_get_last_bits] = (nums2[i] & num_to_get_last_bits)
        
        return mapping
