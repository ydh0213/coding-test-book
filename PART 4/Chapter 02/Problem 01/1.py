def solution(dart_result):
    sdt = ' SDT'
    ans = []
    idx = 0
    for i, c in enumerate(dart_result):
        if c in sdt:
            ans.append(int(dart_result[idx:i]) ** sdt.index(c))
        elif c == '#':
            ans[-1] = -ans[-1]
        elif c == '*':
            ans[-1] <<= 1
            if len(ans) >= 2:
                ans[-2] <<= 1

        if not c.isdecimal():
            idx = i + 1

    return sum(ans)