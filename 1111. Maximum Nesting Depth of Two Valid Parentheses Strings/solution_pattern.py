class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []

        for i, c in enumerate(seq):
            if c == '(':
                res.append(i % 2)
            else:
                res.append(1 - i % 2)
            # The above code can also be abbreviated to
            # ans.append((i & 1) ^ (ch == '('))
            # C++ and JavaScript code provide direct shorthand methods.
        
        return res
