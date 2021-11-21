N = int(input())
arr = list(map(int, input().split()))
stk = []  # index 저장
ans = [-1 for _ in range(N)]
for i in range(N):
    while stk and arr[stk[-1]] < arr[i]:
        ans[stk[-1]] = arr[i]
        stk.pop(-1)

    stk.append(i)

print(' '.join(map(str, ans)))
