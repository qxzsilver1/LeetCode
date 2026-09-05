class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if re.fullmatch(r"[A-Z]*|.[a-z]*", word):
            return True
        else:
            return False
