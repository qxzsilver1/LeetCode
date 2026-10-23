class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mapping = {}

        for r in replacements:
            mapping[r[0]] = r[1]
        
        resolved = {}
        
        def resolve(key):
            if key in resolved:
                return resolved[key]
            
            val = mapping[key]

            if '%' not in val:
                resolved[key] = val
                return val
            
            parts = val.split('%')

            res = []

            for i in range(len(parts)):
                if i % 2 == 0:
                    res.append(parts[i])
                else:
                    res.append(resolve(parts[i]))
            
            resolved[key] = ''.join(res)
            
            return resolved[key]
        
        for key in mapping:
            resolve(key)
        
        parts = text.split('%')

        ans = []

        for i in range(len(parts)):
            if i % 2 == 0:
                ans.append(parts[i])
            else:
                ans.append(resolved[parts[i]])
        
        return ''.join(ans)
