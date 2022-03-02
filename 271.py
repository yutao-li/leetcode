class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(str(len(i)) + ' ' + i for i in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            delimit = s.find(' ', i)
            str_len = int(s[i:delimit])
            i = delimit + str_len + 1
            res.append(s[delimit + 1:i])
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
