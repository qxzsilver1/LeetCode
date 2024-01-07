class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            group_dict[tuple(count)].append(s)
        
        return group_dict.values()
