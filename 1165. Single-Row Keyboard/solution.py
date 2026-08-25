class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_index_map = {}

        for i in range(len(keyboard)):
            key_index_map[keyboard[i]] = i
        
        prev_idx = 0
        
        res = 0

        for c in word:
            res += abs(prev_idx - key_index_map[c])

            prev_idx = key_index_map[c]
        
        return res
