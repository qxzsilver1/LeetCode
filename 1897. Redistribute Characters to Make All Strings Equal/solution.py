class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count_dict = {}
        n = len(words)

        for word in words:
            for c in word:
                count_dict[c] = 1 + count_dict.get(c, 0)

        for val in count_dict.values():
            if val % n != 0:
                return False

        return True 
