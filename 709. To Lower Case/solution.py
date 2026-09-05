class Solution:
    def toLowerCase(self, s: str) -> str:
        isUpper = lambda x: 'A' <= x <= 'Z'
        toLowercase = lambda x: chr(ord(x) | 32)

        return ''.join([toLowercase(x) if isUpper(x) else x for x in s])
