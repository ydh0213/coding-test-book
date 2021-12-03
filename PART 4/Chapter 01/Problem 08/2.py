dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

N, M = map(int, input().split())
beads = [[[0] * N for _ in range(N)] for _ in range(2)]
b = 0
for i in range(N):
    beads[b][i] = list(map(int, input().split()))

coords = [(N // 2, N // 2)]
dr = 0
idx = 1
for dist in range(1, N):
    for _ in range(2):
        for _ in range(dist):
            ny = coords[-1][0] + dy[dr]
            nx = coords[-1][1] + dx[dr]
            coords.append((ny, nx))
            idx += 1

        dr = (dr + 1) % 4

for _ in range(N - 1):
    ny = coords[-1][0] + dy[dr]
    nx = coords[-1][1] + dx[dr]
    coords.append((ny, nx))
    idx += 1

dr = (dr + 1) % 4

ans = 0
for _ in range(M):
    # 1. 구슬 파괴
    d, s = map(int, input().split())
    if d == 1:
        d = 3
    elif d == 2:
        d = 1
    elif d == 3:
        d = 0
    else:
        d = 2

    y, x = coords[0]
    for _ in range(1, s + 1):
        y = y + dy[d]
        x = x + dx[d]
        beads[b][y][x] = 0

    while True:
        for i in range(N):
            for j in range(N):
                beads[b ^ 1][i][j] = 0

        # 2. 빈 칸 구슬 이동
        idx = 1
        ny, nx = coords[idx]
        for i in range(1, N ** 2):
            y, x = coords[i]
            if beads[b][y][x]:
                beads[b ^ 1][ny][nx] = beads[b][y][x]
                idx += 1
                ny, nx = coords[idx]

        b ^= 1

        # 3. 구슬 연속 4개 폭발
        is_there_move = False
        y, x = coords[1]
        bead = beads[b][y][x]
        cnt = 1
        for i in range(2, N ** 2):
            y, x = coords[i]
            if beads[b][y][x] == bead:
                cnt += 1
            else:
                if cnt >= 4:
                    for j in range(i - 1, i - 1 - cnt, -1):
                        ny, nx = coords[j]
                        ans += beads[b][ny][nx]
                        beads[b][ny][nx] = 0
                        is_there_move = True

                bead = beads[b][y][x]
                cnt = 1

                if bead == 0:
                    break

        if not is_there_move:
            break

    for i in range(N):
        for j in range(N):
            beads[b ^ 1][i][j] = 0

    # 4. 구슬이 변화하는 단계
    y, x = coords[1]
    bead = beads[b][y][x]
    cnt = 1
    idx = 1
    ny, nx = coords[idx]
    for i in range(2, N ** 2):
        y, x = coords[i]
        if beads[b][y][x] == bead:
            cnt += 1
        else:
            beads[b ^ 1][ny][nx] = cnt
            idx += 1
            if idx < len(coords):
                ny, nx = coords[idx]
            else:
                break

            beads[b ^ 1][ny][nx] = bead
            idx += 1
            if idx < len(coords):
                ny, nx = coords[idx]
            else:
                break

            bead = beads[b][y][x]
            cnt = 1

            if bead == 0:
                break

    b ^= 1

print(ans)
