class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        def isSubsequence(subsequence_maybe, main_string):
            i = j = 0

            while i < len(subsequence_maybe) and j < len(main_string):
                if subsequence_maybe[i] == main_string[j]:
                    i += 1
                j += 1
            
            return i == len(subsequence_maybe)
        
        source_chars = set(source)

        for c in target:
            if c not in source_chars:
                return -1
        
        concatenated_source = source
        cnt = 1

        while not isSubsequence(target, concatenated_source):
            concatenated_source += source
            cnt += 1
        
        return cnt
