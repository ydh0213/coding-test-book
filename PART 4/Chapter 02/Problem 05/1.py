def is_valid(p):
    stk = []
    for ch in p:
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                return False

    return len(stk) == 0


def solution(p):
    if p == '':
        return p

    cnt = 0
    u = ''
    v = ''
    for i, ch in enumerate(p):
        cnt += 1 if ch == '(' else -1
        if cnt == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    if is_valid(u):
        return u + solution(v)

    res = '(' + solution(v) + ')'
    for ch in u[1:-1]:
        res += ')' if ch == '(' else '('

    return res
