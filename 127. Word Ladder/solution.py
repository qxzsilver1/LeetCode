class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbor_word = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbor_word[pattern].append(word)
        
        visited = set([beginWord])

        q = deque([beginWord])

        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for nei in neighbor_word[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
        
            res += 1
        
        return 0
