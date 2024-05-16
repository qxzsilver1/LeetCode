class Solution:
    def countAndSay(self, n: int) -> str:
        n -= 1
        x = '1'

        def rle_recurse(s):
            st = []

            for g, t in groupby(s):
                st.append(str(len(list(t))) + g)
            
            return ''.join(st)
        
        for _ in range(n):
            x = rle_recurse(x)
        
        return x
