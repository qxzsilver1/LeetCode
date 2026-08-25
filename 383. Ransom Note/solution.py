class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for c in ransom_count:
            if magazine_count[c] < ransom_count[c]:
                return False
        
        return True
