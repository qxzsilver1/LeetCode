class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)

        l, r = 0, len(s) - 1

        offset_l = ord('a')
        offset_r = offset_l + 25

        while l < r:
            if offset_l <= ord(s[l].lower()) <= offset_r and offset_l <= ord(s[r].lower()) <= offset_r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            
            if ord(s[l].lower()) < offset_l or offset_r < ord(s[l].lower()):
                l += 1
            
            if ord(s[r].lower()) < offset_l or offset_r < ord(s[r].lower()):
                r -= 1
        
        return ''.join(s)
