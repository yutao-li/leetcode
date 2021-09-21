"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


def read4(buf):
    pass


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tmp = [0] * 4
        j = 0
        q, r = divmod(n, 4)
        for _ in range(q):
            i = read4(tmp)
            if i != 4:
                buf[j:j + i] = tmp[:i]
                j += i
                return j
            buf[j:j + 4] = tmp
            j += 4
        if r:
            i = read4(tmp)
            k = min(r, i)
            buf[j:j + k] = tmp[:k]
            j += k
        return j
