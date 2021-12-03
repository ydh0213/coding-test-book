dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score = 0
groups = [[0] * N for _ in range(N)]
group_idx = 0
sz = 0
rainbow = 0
block_color = 0


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


def recur(y, x):
    global sz, rainbow
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and groups[ny][nx] == 0:
            if board[ny][nx] == 0:
                sz += 1
                rainbow += 1
                groups[ny][nx] = group_idx
                recur(ny, nx)
            elif board[ny][nx] == block_color:
                sz += 1
                groups[ny][nx] = group_idx
                recur(ny, nx)


def recur_remove(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and board[ny][nx] >= 0 and (board[ny][nx] == 0 or groups[ny][nx] == group_idx):
            board[ny][nx] = -2
            recur_remove(ny, nx)


def pull_down():
    for j in range(N):
        for i in range(N - 1, -1, -1):
            if board[i][j] == -2:
                for k in range(i - 1, -1, -1):
                    if board[k][j] == -1:
                        break

                    if board[k][j] >= 0:
                        board[i][j] = board[k][j]
                        board[k][j] = -2
                        break


def rotate():
    next_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            next_board[i][j] = board[j][N - 1 - i]

    for i in range(N):
        for j in range(N):
            board[i][j] = next_board[i][j]


while True:
    groups = [[0] * N for _ in range(N)]
    group_idx = 0
    candi = []
    for i in range(N):
        for j in range(N):
            if groups[i][j] == 0:
                if board[i][j] < 0:
                    groups[i][j] = board[i][j]
                    continue

                if board[i][j] > 0:
                    # 블록 개수가 2보다 크거나 같은지 체크
                    cnt = 1
                    for k in range(4):
                        ni = i + dy[k]
                        nj = j + dx[k]
                        if is_valid_coord(ni, nj) and (board[ni][nj] == 0 or board[ni][nj] == board[i][j]):
                            cnt += 1

                    if cnt < 2:
                        continue

                    group_idx += 1
                    sz = 0
                    rainbow = 0
                    block_color = board[i][j]
                    groups[i][j] = group_idx
                    sz += 1
                    recur(i, j)
                    candi.append((sz, rainbow, i, j, group_idx))

                    # 무지개 블록은 탐색기록 초기화
                    for y in range(N):
                        for x in range(N):
                            if board[y][x] == 0:
                                groups[y][x] = 0

    if group_idx == 0:
        break

    candi.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))

    score += candi[0][0] ** 2

    group_idx = candi[0][4]
    board[candi[0][2]][candi[0][3]] = -2
    recur_remove(candi[0][2], candi[0][3])

    pull_down()
    rotate()
    pull_down()

print(score)
