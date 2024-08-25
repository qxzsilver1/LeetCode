class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        buckets = [[] for _ in range(15)]
        res = []

        for n in arr:
            num = n
            num_ones = 0

            while n:
                n &= (n - 1)
                num_ones += 1
            
            buckets[num_ones].append(num)
        
        for bucket in buckets:
            bucket.sort()

            for num in bucket:
                res.append(num)
        
        return res
