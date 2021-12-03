dy = (-1, -1, 1, 1)
dx = (-1, 1, -1, 1)
ddy = (0, -1, -1, -1, 0, 1, 1, 1)
ddx = (-1, -1, 0, 1, 1, 1, 0, -1)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
clouds = [[[False] * N for _ in range(N)] for _ in range(2)]
c = 0
for i in range(N - 2, N):
    for j in range(2):
        clouds[c][i][j] = True


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


for _ in range(M):
    d, s = map(int, input().split())
    for y in range(N):
        for x in range(N):
            if clouds[c][y][x]:
                ny = (y + ddy[d - 1] * s + N * 50) % N
                nx = (x + ddx[d - 1] * s + N * 50) % N
                clouds[c ^ 1][ny][nx] = True
                A[ny][nx] += 1

    for y in range(N):
        for x in range(N):
            if clouds[c ^ 1][y][x]:
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if is_valid_coord(ny, nx) and A[ny][nx]:
                        A[y][x] += 1

    for y in range(N):
        for x in range(N):
            if not clouds[c ^ 1][y][x] and A[y][x] >= 2:
                A[y][x] -= 2
                clouds[c][y][x] = True
            else:
                clouds[c][y][x] = False

    for y in range(N):
        for x in range(N):
            clouds[c ^ 1][y][x] = False

print(sum(sum(i) for i in A))
