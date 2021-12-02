dy = (0, 0, 0, -1, 1)
dx = (0, 1, -1, 0, 0)

N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [0, 0, 0, 0, 0, 0, 0]


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


for cmd in list(map(int, input().split())):
    ny = y + dy[cmd]
    nx = x + dx[cmd]
    if not is_valid_coord(ny, nx):
        continue

    next_dice = dice[:]
    if cmd == 1:  # 동쪽
        next_dice[1] = dice[4]
        next_dice[3] = dice[1]
        next_dice[6] = dice[3]
        next_dice[4] = dice[6]
    elif cmd == 2:  # 서쪽
        next_dice[1] = dice[3]
        next_dice[3] = dice[6]
        next_dice[6] = dice[4]
        next_dice[4] = dice[1]
    elif cmd == 3:  # 북쪽
        next_dice[1] = dice[5]
        next_dice[2] = dice[1]
        next_dice[6] = dice[2]
        next_dice[5] = dice[6]
    else:  # 남쪽
        next_dice[1] = dice[2]
        next_dice[2] = dice[6]
        next_dice[6] = dice[5]
        next_dice[5] = dice[1]

    dice = next_dice[:]
    if board[ny][nx] == 0:
        board[ny][nx] = dice[6]
    else:
        dice[6] = board[ny][nx]
        board[ny][nx] = 0

    y = ny
    x = nx
    print(dice[1])
