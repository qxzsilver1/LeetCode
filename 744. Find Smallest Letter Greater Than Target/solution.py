class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = ord('z') + 1
        l, r = 0, len(letters)-1

        while l <= r:
            m = l + (r - l) // 2

            if ord(letters[m]) > ord(target):
                idx = ord(letters[m]) if idx > ord(letters[m]) else idx
                r = m - 1
            else:
                l = m + 1
        
        return chr(idx) if idx != ord('z') + 1 else letters[0]
