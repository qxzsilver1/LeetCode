class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums))] 

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for num, c in counts.items():
            freq[c-1].append(num)
        
        output_arr = []

        for i in range(len(nums) - 1, -1, -1):
            for num in freq[i]:
                output_arr.append(num)

                if len(output_arr) == k:
                    return output_arr
