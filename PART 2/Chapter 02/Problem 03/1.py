N = int(input())
board = [list(input()) for _ in range(N)]
ans = 1


def search():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j - 1] == board[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

    for j in range(N):
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
            search()
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 원상복구

        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            search()
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 원상복구

print(ans)
