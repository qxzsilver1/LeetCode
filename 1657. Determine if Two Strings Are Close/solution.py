class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_dict = Counter(word1)
        word2_dict = Counter(word2)

        val1_sorted = sorted(word1_dict.values())
        val2_sorted = sorted(word2_dict.values())

        word1_chars = set(word1_dict.keys())
        word2_chars = set(word2_dict.keys())

        return word1_chars == word2_chars and val1_sorted == val2_sorted
