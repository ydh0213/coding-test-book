from itertools import groupby, chain

dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

N, M = map(int, input().split())
beads = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def make_coords():
    ret = [(N // 2, N // 2)]
    d = 0
    for s in range(1, N + 1):
        for _ in range(2):
            for _ in range(s):
                y, x = ret[-1]
                y += dy[d]
                x += dx[d]
                ret.append((y, x))
                if len(ret) >= N * N:
                    return ret

            d = (d + 1) % 4


coords = make_coords()
for _ in range(M):
    d, s = map(int, input().split())
    if d == 1:
        d = 3
    elif d == 2:
        d = 1
    elif d == 3:
        d = 0
    else:
        d = 2

    # 구슬 파괴
    y, x = coords[0]
    for i in range(1, s + 1):
        y += dy[d]
        x += dx[d]
        beads[y][x] = 0

    # 구슬 이동 및 폭발
    arr = [[] for _ in range(2)]
    b = 0
    for y, x in coords:
        if beads[y][x]:
            arr[b].append(beads[y][x])

    while True:
        is_boomed = False
        for bead, gr in groupby(arr[b]):
            tmp = list(gr)
            if len(tmp) >= 4:
                is_boomed = True
                ans += bead * len(tmp)
            else:
                arr[b ^ 1] += tmp

        arr[b].clear()
        b ^= 1

        if not is_boomed:
            break

    for i in range(N):
        for j in range(N):
            beads[i][j] = 0

    # 구슬 변화
    nxt = chain.from_iterable((len(list(gr)), bead) for bead, gr in groupby(arr[b]))
    for (y, x), val in zip(coords[1:], nxt):
        beads[y][x] = val

print(ans)
