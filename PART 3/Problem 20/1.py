N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
acc = [[0] * N for _ in range(N)]
ans = 0


def get_area(a, b, c, d):
    ret = acc[c][d]
    if a:
        ret -= acc[a - 1][d]

    if b:
        ret -= acc[c][b - 1]

    if a and b:
        ret += acc[a - 1][b - 1]

    return ret


def f():
    global ans
    acc[0][0] = board[0][0]
    for j in range(1, N):
        acc[0][j] = acc[0][j - 1] + board[0][j]

    for i in range(1, N):
        acc[i][0] = acc[i - 1][0] + board[i][0]
        for j in range(1, N):
            acc[i][j] = acc[i][j - 1] + acc[i - 1][j] - acc[i - 1][j - 1] + board[i][j]

    for y in range(1, N):
        for x in range(1, N):
            cnt = dict()
            for i in range(y):
                for j in range(x):
                    area = get_area(i, j, y - 1, x - 1)
                    if area in cnt:
                        cnt[area] += 1
                    else:
                        cnt[area] = 1

            for i in range(y, N):
                for j in range(x, N):
                    area = get_area(y, x, i, j)
                    if area in cnt:
                        ans += cnt[area]


f()
for i in range(N):
    board[i].reverse()

f()

print(ans)
