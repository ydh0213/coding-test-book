ans = 0
for _ in range(int(input())):
    stk = []
    for ch in input():
        if not stk or stk[-1] != ch:
            stk.append(ch)
        else:
            stk.pop()

    ans += len(stk) == 0

print(ans)
