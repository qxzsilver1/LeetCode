class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word_idx in range(len(words)):
            for char_pos in range(len(words[word_idx])):
                if char_pos >= len(words) or word_idx >= len(words[char_pos]) or words[word_idx][char_pos] != words[char_pos][word_idx]:
                    return False
        
        return True
