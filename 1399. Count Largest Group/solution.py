class Solution:
    def countLargestGroup(self, n: int) -> int:
        int_groups = Counter()

        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            int_groups[key] += 1
        
        max_val = max(int_groups.values())
        cnt = sum(1 for v in int_groups.values() if max_val == v)

        return cnt
