N, K = map(int, input().split())
peo = [i for i in range(1, N + 1)]
pt = 0
ans = []
for _ in range(N):
    pt += K - 1
    pt %= len(peo)
    ans.append(peo.pop(pt))

print(f"<{', '.join(map(str, ans))}>")
