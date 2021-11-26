from collections import deque

dz = (0, 0, 0, 0, 1, -1)
dy = (0, 1, 0, -1, 0, 0)
dx = (1, 0, -1, 0, 0, 0)

while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break

    b = []
    for _ in range(L):
        b.append([input() for _ in range(R)])
        input()  # blank line


    def get_start():
        for i in range(L):
            for j in range(R):
                for k in range(C):
                    if b[i][j][k] == 'S':
                        return i, j, k


    def is_valid_coord(z, y, x):
        return 0 <= z < L and 0 <= y < R and 0 <= x < C


    def bfs(sz, sy, sx):
        chk = [[[False] * C for _ in range(R)] for _ in range(L)]
        chk[sz][sy][sx] = True
        dq = deque()
        dq.append((sz, sy, sx, 0))
        while dq:
            z, y, x, d = dq.popleft()

            if b[z][y][x] == 'E':
                return d

            for k in range(6):
                nz = z + dz[k]
                ny = y + dy[k]
                nx = x + dx[k]
                nd = d + 1
                if is_valid_coord(nz, ny, nx) and b[nz][ny][nx] != '#' and not chk[nz][ny][nx]:
                    chk[nz][ny][nx] = True
                    dq.append((nz, ny, nx, nd))

        return 0


    sz, sy, sx = get_start()
    ans = bfs(sz, sy, sx)
    print(f'Escaped in {ans} minute(s).' if ans else 'Trapped!')
