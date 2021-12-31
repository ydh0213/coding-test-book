N = int(input())
board = list(list(input()) for _ in range(N))
ans = 1


def search(y, x):
    global ans
    for i in range(y, y + 2):
        if i < N:
            cnt = 1
            for j in range(1, N):
                if board[i][j - 1] == board[i][j]:
                    cnt += 1
                    ans = max(ans, cnt)
                else:
                    cnt = 1

    for j in range(x, x + 2):
        if j < N:
            cnt = 1
            for i in range(1, N):
                if board[i - 1][j] == board[i][j]:
                    cnt += 1
                    ans = max(ans, cnt)
                else:
                    cnt = 1


for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            search(i, j)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            search(i, j)
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(ans)
