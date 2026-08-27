class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def getHash(s):
            key = []

            for a, b in zip(s, s[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            
            return ''.join(key)
        
        groups = defaultdict(list)

        for s in strings:
            hash_key = getHash(s)
            groups[hash_key].append(s)
        
        return list(groups.values())
