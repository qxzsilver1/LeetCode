class Solution:
    def generateSentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        for a, b in synonyms:
            union(a, b)

        groups = {}
        for word in list(parent.keys()):
            root = find(word)
            groups.setdefault(root, [])
            if word not in groups[root]:
                groups[root].append(word)
        for root in groups:
            groups[root].sort()

        words = text.split(" ")
        result = []

        def backtrack(i):
            if i == len(words):
                result.append(" ".join(words))
                return

            root = find(words[i]) if words[i] in parent else None

            if root is not None and root in groups:
                original = words[i]
                for syn in groups[root]:
                    words[i] = syn
                    backtrack(i + 1)
                words[i] = original
            else:
                backtrack(i + 1)

        backtrack(0)
        result.sort()
        return result
