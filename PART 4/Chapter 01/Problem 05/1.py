dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N = int(input())
students = [tuple(map(int, input().split())) for _ in range(N ** 2)]
board = [[[0] * 5 for _ in range(N)] for _ in range(N)]


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


for student in students:
    num, fav = student[0], student[1:]
    seats = [[[0] * 2 for _ in range(N)] for _ in range(N)]  # 각 빈칸들에 대해서 인접칸에 좋아하는 학생 수의 합, 빈 칸의 합 저장
    for y in range(N):
        for x in range(N):
            if board[y][x][0] == 0:
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if is_valid_coord(ny, nx):
                        if board[ny][nx][0] == 0:
                            seats[y][x][1] += 1
                        elif board[ny][nx][0] in fav:
                            seats[y][x][0] += 1

    candi = []
    for y in range(N):
        for x in range(N):
            if board[y][x][0] == 0:
                candi.append((seats[y][x][0], seats[y][x][1], y, x))

    candi.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    board[candi[0][2]][candi[0][3]] = student

ans = 0
for y in range(N):
    for x in range(N):
        cnt = 0
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx][0] in board[y][x][1:]:
                cnt += 1

        if cnt > 0:
            ans += 10 ** (cnt - 1)

print(ans)
