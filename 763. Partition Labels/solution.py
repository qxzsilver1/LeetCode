class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}

        for i, c in enumerate(s):
            last_idx[c] = i
        
        res = []

        partition_size, partition_end = 0, 0
        
        for i, c in enumerate(s):
            partition_size += 1

            partition_end = max(partition_end, last_idx[c])

            if i == partition_end:
                res.append(partition_size)
                partition_size = 0
        
        return res

