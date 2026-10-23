class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        
        for mask in range(1 << len(word)):
            parts, count = [], 0
            
            for i, c in enumerate(word):
                if mask & (1 << i): count += 1
                else:
                    if count: parts.append(str(count))
                    parts.append(c)
                    count = 0
            if count: parts.append(str(count))
            result.append(''.join(parts))
        return result
