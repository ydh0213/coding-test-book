# BOJ에서 Python3로 통과

N = int(input())
ans = 0
col = [False] * N  # i번째 열에 퀸을 뒀는지
d1 = [False] * 2 * N  # \ 대각선, 우상단부터 0
d2 = [False] * 2 * N  # / 대각선, 좌상단부터 0


def backtracking(row):
    global ans
    if row == N:
        ans += 1
        return

    for j in range(N if row else N // 2):
        if not col[j] and not d1[row - j] and not d2[row + j]:
            col[j] = True
            d1[row - j] = True
            d2[row + j] = True

            backtracking(row + 1)

            d2[row + j] = False
            d1[row - j] = False
            col[j] = False


if N % 2:
    # 홀수일 때 첫번째 행에 퀸을 왼쪽 절반만 둬보고 그 때의 경우의 수를 2배로 취해준다 (정가운데 제외)
    backtracking(0)
    ans *= 2

    # 첫번째 행의 정가운데에 퀸을 뒀을 때의 경우의 수를 구해서 더해준다
    j = N // 2
    col[j] = d1[-j] = d2[j] = True
    backtracking(1)

    print(ans)
else:
    # 짝수일 때 첫번째 행에 퀸을 왼쪽 절반만 둬보고 그 떄의 경우의 수를 2배로 취해준다
    backtracking(0)
    print(ans * 2)
