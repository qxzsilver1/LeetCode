class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        close_cnt = 0

        for c in s:
            if c == '(':
                open_cnt += 1
            else:
                open_cnt -= 1

                if open_cnt < 0:
                    open_cnt = 0
                    close_cnt += 1

        return open_cnt + close_cnt
