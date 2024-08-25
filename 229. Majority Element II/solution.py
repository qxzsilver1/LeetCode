class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

            if len(counts) <= 2:
                continue
            
            new_count = defaultdict(int)

            for n, c in counts.items():
                if c > 1:
                    new_count[n] = c - 1
            
            counts = new_count
        
        res = []

        for n in counts:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res
