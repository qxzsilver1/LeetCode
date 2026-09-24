class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()

        mp = defaultdict(list)
        
        for time, user, site in arr:
            mp[user].append(site)
        
        count = defaultdict(int)
        
        for user in mp:
            patterns = set()
            cur = mp[user]
            
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    for k in range(j + 1, len(cur)):
                        patterns.add((cur[i], cur[j], cur[k]))
            for p in patterns:
                count[p] += 1
        
        max_count = 0
        res = tuple()
        
        for pattern in count:
            if count[pattern] > max_count or (count[pattern] == max_count and pattern < res):
                max_count = count[pattern]
                res = pattern

        return list(res)
