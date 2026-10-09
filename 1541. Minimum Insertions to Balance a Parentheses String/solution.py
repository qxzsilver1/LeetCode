class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        insertions = 0
        left_cnt, idx = 0, 0

        while idx < n:
            if s[idx] == "(":
                left_cnt += 1
                idx += 1
            else:
                if left_cnt > 0:
                    left_cnt -= 1
                else:
                    insertions += 1
                
                if idx < n - 1 and s[idx + 1] == ")":
                    idx += 2
                else:
                    insertions += 1
                    idx += 1
        
        insertions += 2 * left_cnt

        return insertions
