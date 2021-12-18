for _ in range(int(input())):
    stk = []
    ans = 'YES'
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            if len(stk) > 0:
                stk.pop()
            else:
                ans = 'NO'

    if len(stk) > 0:
        ans = 'NO'

    print(ans)
