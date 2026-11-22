class Solution:
    def checkString(self, s: str) -> bool:
        a_appears = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'a':
                a_appears = True
            
            if s[i] == 'b':
                if a_appears:
                    return False
                continue
        return True
