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
                temp_path = list(curr_path)
                shortest_paths.append(temp_path)
            
            for i in range(len(adj_list.get(src, []))):
                curr_path.append(adj_list[src][i])
                backtrack(adj_list[src][i], dst)
                curr_path.pop()
        
        def addEdge(word1, word2, direction):
            if direction == 1:
                adj_list[word1] = adj_list.get(word1, []) + [word2]
            else:
                adj_list[word2] = adj_list.get(word2, []) + [word1]
        
        def bfs():
            if endWord not in wordSet:
                return False
            
            if beginWord in wordSet:
                wordSet.remove(beginWord)
            
            qb, qe = set([beginWord]), set([endWord])

            found = False
            direction = 1

            while qb:
                visited = set()

                if len(qb) > len(qe):
                    qb, qe = qe, qb
                    direction ^= 1

                for curr_word in qb:
                    neighbors = findNeighbors(curr_word)

                    for nei in neighbors:
                        if nei in qe:
                            found = True
                            addEdge(curr_word, nei, direction)
                        elif not found and nei in wordSet and nei not in qb:
                            visited.add(nei)
                            addEdge(curr_word, nei, direction)
                
                for curr_word in qb:
                    if curr_word in wordSet:
                        wordSet.remove(curr_word)
                
                if found:
                    break
                
                qb = visited
            return found
        
        sequence_found = bfs()

        if sequence_found == False:
            return shortest_paths

        curr_path.append(beginWord)
        backtrack(beginWord, endWord)

        return shortest_paths
