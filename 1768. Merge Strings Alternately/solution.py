class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        output = []

        while i < len(word1) and j < len(word2):
            output.append(word1[i])
            i += 1
            output.append(word2[j])
            j += 1
        
        if i < len(word1):
            output.append(word1[i:])
        
        if j < len(word2):
            output.append(word2[j:])
        
        return ''.join(output)
