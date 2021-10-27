n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
ans = max(arr[0])
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1]) + 1

    ans = max(ans, max(arr[i]))

print(ans ** 2)
