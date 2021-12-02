from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
sry, srx, sby, sbx = -1, -1, -1, -1
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            sry, srx = i, j
        elif board[i][j] == 'B':
            sby, sbx = i, j


def go_next(ry, rx, by, bx, k):
    nry, nrx, nby, nbx = ry, rx, by, bx

    while True:
        nry = nry + dy[k]
        nrx = nrx + dx[k]
        if board[nry][nrx] == 'O':
            nry, nrx = -1, -1
            break
        elif board[nry][nrx] == '#':
            nry = nry - dy[k]
            nrx = nrx - dx[k]
            break

    while True:
        nby = nby + dy[k]
        nbx = nbx + dx[k]
        if board[nby][nbx] == 'O':
            nby, nbx = -1, -1
            break
        elif board[nby][nbx] == '#':
            nby = nby - dy[k]
            nbx = nbx - dx[k]
            break

    # 구슬들이 구멍에 빠지지 않았으면서 충돌했을 경우
    if nry != -1 and nry == nby and nrx == nbx:
        if k == 0:
            if rx < bx:
                nrx -= 1
            else:
                nbx -= 1
        elif k == 1:
            if ry < by:
                nry -= 1
            else:
                nby -= 1
        elif k == 2:
            if bx < rx:
                nrx += 1
            else:
                nbx += 1
        else:
            if by < ry:
                nry += 1
            else:
                nby += 1

    return nry, nrx, nby, nbx


def bfs():
    chk = set()
    dq = deque()
    chk.add((sry, srx, sby, sbx))
    dq.append((sry, srx, sby, sbx, 0))
    while dq:
        ry, rx, by, bx, d = dq.popleft()
        if by == -1 and bx == -1:  # 파란 구슬이 구멍에 빠지면 실패
            continue

        if ry == -1 and rx == -1:
            return d

        if d < 10:
            nd = d + 1
            for k in range(4):
                nry, nrx, nby, nbx = go_next(ry, rx, by, bx, k)
                if (nry, nrx, nby, nbx) not in chk:
                    chk.add((nry, nrx, nby, nbx))
                    dq.append((nry, nrx, nby, nbx, nd))

    return -1


print(bfs())
