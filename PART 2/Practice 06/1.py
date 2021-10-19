# BOJ에서 PyPy3만 통과하며 Python3는 시간초과 발생

N = int(input())
ans = 0
col = [False] * N  # i번째 열에 퀸을 뒀다
d1 = [False] * 2 * N  # \ 대각선, 우상단부터 0
d2 = [False] * 2 * N  # / 대각선, 좌상단부터 0


# Backtracking
def bt(row):
    global ans
    if row == N:
        ans += 1
        return

    for j in range(N):
        if not col[j] and not d1[row - j] and not d2[row + j]:
            col[j] = True
            d1[row - j] = True
            d2[row + j] = True

            bt(row + 1)

            # 원상복구
            d2[row + j] = False
            d1[row - j] = False
            col[j] = False


bt(0)
print(ans)
