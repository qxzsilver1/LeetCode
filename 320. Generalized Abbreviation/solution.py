class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []

        def backtrack(i, curr, count):
            if i == len(word):
                if count:
                    curr.append(str(count))
                    res.append(''.join(curr[:]))

                    curr.pop()
                else:
                    res.append(''.join(curr[:]))
                
                return
            
            backtrack(i+1, curr, count+1)


            str_app = str(count) + word[i] if count else word[i]
            
            curr.append(str_app)
            
            backtrack(i+1, curr, 0)
            curr.pop()
        
        backtrack(0, [], 0)

        return res
