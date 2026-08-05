class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        j = 0
        cnt = 0
        ans = ""

        while j < n:
            if s[j] == '1':
                cnt += 1

            if cnt == k:
                while i < n and cnt == k:
                    temp = s[i:j + 1]
                    if not ans or len(ans) > len(temp):
                        ans = temp
                    elif len(ans) == len(temp):
                        ans = min(ans, temp)

                    if s[i] == '1':
                        cnt -= 1
                    i += 1

            j += 1

        return ans
