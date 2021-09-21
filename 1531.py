from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        count = 1
        ps = [('', 1)]
        for ch1, ch2 in zip(s[1:], s):
            if ch1 == ch2:
                count += 1
            else:
                ps.append((ch2, count))
                count = 1
        ps.append((s[-1], count))
        post_sum = [0] * (len(ps) + 1)
        for i in range(len(ps) - 1, -1, -1):
            post_sum[i] = post_sum[i + 1] + 1
            if ps[i][1] != 1:
                post_sum[i] += len(str(ps[i][1]))

        @lru_cache(None)
        def dfs(count, ch, index, left):
            cur, ct = ps[index]
            acc = 1 if count == 1 else len(str(count)) + 1
            if index == len(ps) - 1:
                l = ct - left
                if l <= 0:
                    return acc
                else:
                    if ch == cur:
                        count += l
                        return len(str(count)) + 1
                    else:
                        return acc + 1 + (len(str(l)) if l != 1 else 0)
            else:
                if cur == ch:
                    return dfs(count + ct, cur, index + 1, left)
                else:
                    keep = acc + dfs(ct, cur, index + 1, left)
                    if ct >= left:
                        if ct > left:
                            ct -= left
                            acc += 1 if ct == 1 else 1 + len(str(ct))
                        else:
                            next_ch, next_ct = ps[index + 1]
                            if ch == next_ch:
                                count += next_ct
                                acc = 1 + len(str(count))
                                index += 1
                        discard = acc + post_sum[index + 1]
                    else:
                        discard = dfs(count, ch, index + 1, left - ct)
                    return min(keep, discard)

        return dfs(1, '', 1, k) - 1


res = Solution().getLengthOfOptimalCompression("llllllllllttttttttt", 1)
