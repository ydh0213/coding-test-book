from itertools import groupby


def solution(s):
    ans = len(s)
    for n in range(1, len(s) // 2 + 1):
        res = ''
        for cutted, group in groupby([s[i:i + n] for i in range(0, len(s), n)]):
            dup_n = len(list(group))
            res += str(dup_n) + cutted if dup_n >= 2 else cutted

        ans = min(ans, len(res))

    return ans