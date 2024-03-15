class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left_palindrome = set()
        right_palindrome = collections.Counter(s)

        for i in range(len(s)):
            right_palindrome[s[i]] -= 1

            if right_palindrome[s[i]] == 0:
                right_palindrome.pop(s[i])

            for j in range(26):
                c = chr(ord('a') + j)

                if c in left_palindrome and c in right_palindrome:
                    res.add((s[i], c))
            
            left_palindrome.add(s[i])

        return len(res)
