class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        max_count = max(counts.values())

        buckets = [0] * (max_count + 1)

        for count in counts.values():
            buckets[count] += 1
        
        set_cardinality = 0
        count_to_remove = len(arr) // 2
        bucket = max_count

        while count_to_remove > 0:
            max_needed_from_bucket = math.ceil(count_to_remove / bucket)
            set_cardinality_incr = min(buckets[bucket], max_needed_from_bucket)
            set_cardinality += set_cardinality_incr

            count_to_remove -= set_cardinality_incr * bucket
            bucket -= 1
        
        return set_cardinality
