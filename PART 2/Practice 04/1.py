import sys
sys.setrecursionlimit(10 ** 6)

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M, K = map(int, input().split())
board = [['.'] * M for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = '#'

visited = [[False] * M for _ in range(N)]
sz = 0
ans = 0


def isValidCoord(y, x):
    return 0 <= y < N and 0 <= x < M


def dfs(y, x):
    global ans, sz

    visited[y][x] = True
    sz += 1
    ans = max(ans, sz)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if isValidCoord(ny, nx) and not visited[ny][nx] and board[ny][nx] == '#':
            dfs(ny, nx)


for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == '#':
            sz = 0
            dfs(i, j)

print(ans)
