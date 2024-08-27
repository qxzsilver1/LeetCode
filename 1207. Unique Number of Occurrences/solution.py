class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = Counter(arr)

        return len(count_dict.keys()) == len(set(count_dict.values()))
