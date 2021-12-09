from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < 5 and 0 <= x < 5


def bfs(sy, sx, place):
    chk = [[False] * 5 for _ in range(5)]
    chk[sy][sx] = True
    dq = deque()
    dq.append((sy, sx, 0))
    while dq:
        y, x, d = dq.popleft()
        if d and place[y][x] == 'P':
            return False

        if d < 2:
            nd = d + 1
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if is_valid_coord(ny, nx) and place[ny][nx] != 'X' and not chk[ny][nx]:
                    chk[ny][nx] = True
                    dq.append((ny, nx, nd))

    return True


def is_ok(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not bfs(i, j, place):
                    return 0

    return 1


def solution(places):
    return [is_ok(place) for place in places]
