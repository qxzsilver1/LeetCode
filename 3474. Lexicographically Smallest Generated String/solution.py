class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        s = ['a'] * (n + m - 1)
        is_fixed = [False] * (n + m - 1)

        for i, ch in enumerate(str1):
            if ch == 'T':
                for j, c in enumerate(str2, i):
                    if is_fixed[j] and s[j] != c:
                        return ''
                    s[j] = c
                    is_fixed[j] = True
        
        for i, ch in enumerate(str1):
            if ch == 'F':
                if any(str2[j-i] != s[j] for j in range(i, i+m)):
                    continue
                
                for j in range(i + m - 1, i-1, -1):
                    if not is_fixed[j]:
                        s[j] = 'b'
                        break
                else:
                    return ''
        
        return ''.join(s)
