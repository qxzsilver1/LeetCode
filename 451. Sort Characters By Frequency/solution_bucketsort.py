class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = Counter(s)
        buckets = defaultdict(list)

        for char, cnt in count_dict.items():
            buckets[cnt].append(char)
        
        res = []

        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)
        
        return ''.join(res)