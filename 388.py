import re


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        cr = re.compile('\n')
        no_tab = re.compile('[^\t]')

        def dfs(start, depth):
            max_len = 0
            pos = start
            while True:
                left = pos
                match = cr.search(input, pos)
                if not match:
                    if '.' in input[pos:]:
                        max_len = max(max_len, len(input) - left)
                    return max_len, len(input), 0
                count_l = match.start() - left
                pos = match.start() + 1
                is_file = '.' in input[left:pos]
                left = pos
                pos = no_tab.search(input, pos).start()
                count_t = pos - left
                if count_t < depth:
                    if is_file:
                        max_len = max(max_len, count_l)
                    return max_len, pos, count_t
                elif count_t == depth:
                    if is_file:
                        max_len = max(max_len, count_l)
                else:
                    sub_l, next_pos, next_depth = dfs(pos, depth + 1)
                    if sub_l:
                        max_len = max(max_len, count_l + sub_l + 1)
                    if next_depth < depth:
                        return max_len, next_pos, next_depth
                    else:
                        pos = next_pos

        return dfs(0, 0)[0]


print(Solution().lengthLongestPath("a"))
