class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count_dict = defaultdict(int)
        n = len(words)

        for word in words:
            for c in word:
                count_dict[c] += 1

        for val in count_dict.values():
            if val % n:
                return False

        return True 
