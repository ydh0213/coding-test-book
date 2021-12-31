from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

R, C = map(int, input().split())
board = [input() for _ in range(R)]
chk = [[set() for _ in range(C)] for _ in range(R)]
ans = 0


def is_valid_coord(y, x):
    return 0 <= y < R and 0 <= x < C


dq = deque()
chk[0][0].add(board[0][0])
dq.append((0, 0, board[0][0]))
while dq:
    y, x, s = dq.popleft()
    ans = max(ans, len(s))

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and board[ny][nx] not in s:
            ns = s + board[ny][nx]
            if ns not in chk[ny][nx]:
                chk[ny][nx].add(ns)
                dq.append((ny, nx, ns))

print(ans)
