class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        max_count = max(counts.values())

        max_count_num = sum(1 for cnt in counts.values() if cnt == max_count)

        num_intervals = (n + 1) * (max_count - 1) + max_count_num

        return max(num_intervals, len(tasks))


