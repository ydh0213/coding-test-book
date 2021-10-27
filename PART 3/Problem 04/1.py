from collections import deque

N, M = map(int, input().split())
gr = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    gr[a - 1][b - 1] = gr[b - 1][a - 1] = True

ans = -1
ans_tot = 987654321
dist = [[0] * N for _ in range(N)]


def bfs(start, goal):
    chk = [False] * N
    dq = deque()
    chk[start] = True
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d

        for nxt in range(N):
            if gr[now][nxt] and not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, d + 1))


for i in range(N):
    tot = 0
    for j in range(N):
        if i != j:
            if dist[i][j] == 0:
                dist[i][j] = dist[j][i] = bfs(i, j)

            tot += dist[i][j]

    if ans_tot > tot:
        ans = i
        ans_tot = tot

print(ans + 1)
