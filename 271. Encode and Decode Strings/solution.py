class Codec:
    delim = '#'

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        res = ''

        for s in strs:
            res += str(len(s)) + self.delim + s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != self.delim:
                j += 1
            
            str_len = int(s[i:j])
            res.append(s[j + 1: j + 1 + str_len])

            i = j + 1 + str_len
        
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
