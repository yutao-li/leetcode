class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        prefix = [0]
        for line in input.splitlines():
            path = line.lstrip('\t')
            depth = len(line) - len(path)
            length = prefix[depth] + len(path)
            if '.' in path:
                res = max(res, length + depth)
            else:
                if depth + 1 < len(prefix):
                    prefix[depth + 1] = length
                else:
                    prefix.append(length)
        return res
