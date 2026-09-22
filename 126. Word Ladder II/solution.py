class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if endWord not in wordList or beginWord == endWord:
            return []
        
        wordSet = set(wordList)
        
        adj_list = {}
        curr_path = []

        shortest_paths = []

        def findNeighbors(word):
            neighbors = []
            char_list = list(word)

            for i in range(len(char_list)):
                old_char = char_list[i]

                for j in range(97, 123):
                    c = chr(j)
                    char_list[i] = c
                    new_word = ''.join(char_list)

                    if c == old_char or new_word not in wordSet:
                        continue
                    neighbors.append(new_word)
                
                char_list[i] = old_char
            
            return neighbors
        
        def backtrack(src, dst):
            if src == dst:
                temp_path = curr_path.copy()
                temp_path.reverse()
                shortest_paths.append(temp_path)
            
            if src not in adj_list:
                return
            
            for nei in adj_list[src]:
                curr_path.append(nei)
                backtrack(nei, dst)
                curr_path.pop()
        
        def bfs():
            q = deque([beginWord])
            wordSet.discard(beginWord)

            is_enqueued = {beginWord: True}

            while q:
                visited = []

                for _ in range(len(q)):
                    curr_word = q.popleft()
                    neighbors = findNeighbors(curr_word)

                    for nei in neighbors:
                        visited.append(nei)

                        if nei not in adj_list:
                            adj_list[nei] = []
                        
                        adj_list[nei].append(curr_word)

                        if nei not in is_enqueued:
                            q.append(nei)
                            is_enqueued[nei] = True

                for word in visited:
                    wordSet.discard(word)
        bfs()

        curr_path = [endWord]
        backtrack(endWord, beginWord)

        return shortest_paths
