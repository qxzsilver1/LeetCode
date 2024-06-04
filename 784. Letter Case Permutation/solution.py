class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(i, curr):
            if i == len(s):
                res.append(''.join(curr[:]))
                return
            
            curr.append(s[i])
            backtrack(i+1, curr)
            curr.pop()
            
            if s[i].isalpha():
                curr.append(s[i].swapcase())
                backtrack(i+1, curr)
                curr.pop()
        
        backtrack(0, [])

        return res
