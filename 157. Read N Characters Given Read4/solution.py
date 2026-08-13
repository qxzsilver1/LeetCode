"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copied_chars = 0
        read_chars = 4
        remaining_chars = n

        while remaining_chars >= 4 and read_chars == 4:
            buf4 = [''] * 4
            read_chars = read4(buf4)

            for i in range(read_chars):
                buf[copied_chars + i] = buf4[i]
            
            copied_chars += read_chars
        
        if remaining_chars > 0 and read_chars != 0:
            buf4 = [''] * 4
            read_chars = read4(buf4)

            for i in range(min(remaining_chars, read_chars)):
                buf[copied_chars + i] = buf4[i]
            
            copied_chars += read_chars
        
        return min(n, copied_chars)
