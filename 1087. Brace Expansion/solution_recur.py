class Solution:
    def expand(self, s: str) -> list[str]:
        def storeFirstOptions(startPos, firstOptions):
            # If the first character is not '{', it means a single character
            if s[startPos] != '{':
                firstOptions.append(s[startPos])
            else:
                # Store all the characters between '{' and '}'
                while s[startPos] != '}':
                    if 'a' <= s[startPos] <= 'z':
                        firstOptions.append(s[startPos])
                    startPos += 1
                # Sort the list
                firstOptions.sort()
            # Increment it to point to the next character to be considered
            return startPos + 1

        def findAllWords(startPos):
            # Return empty string list if the string is empty
            if startPos == len(s):
                return [""]

            firstOptions = []
            # Store the characters for the first index as string in firstOptions
            remStringStartPos = storeFirstOptions(startPos, firstOptions)
            wordsWithRemString = findAllWords(remStringStartPos)

            expandedWords = []
            # Create new words by adding the character at the beginning
            for c in firstOptions:
                for word in wordsWithRemString:
                    expandedWords.append(c + word)

            return expandedWords

        return findAllWords(0)
