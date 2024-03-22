class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr_line, curr_line_length = [], 0

        i = 0

        while i < len(words):

            if curr_line_length + len(curr_line) + len(words[i]) > maxWidth:
                # line complete
                
                extra_spaces = maxWidth - curr_line_length

                spaces = extra_spaces // max(len(curr_line) - 1, 1)
                remainder = extra_spaces % max(len(curr_line) - 1, 1)

                for j in range(max(1, len(curr_line) - 1)):
                    curr_line[j] += ' ' * spaces

                    if remainder:
                        curr_line[j] += ' '
                        remainder -= 1


                res.append(''.join(curr_line))
                curr_line, curr_line_length = [], 0 # reset line and line length

            curr_line.append(words[i])
            curr_line_length += len(words[i])
            i += 1
        
        # handle last line
        last_line = ' '.join(curr_line)
        trailing_spaces = maxWidth - len(last_line)
        
        res.append(last_line + ' ' * trailing_spaces)

        return res
