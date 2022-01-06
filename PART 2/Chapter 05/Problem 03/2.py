import sys

sys.setrecursionlimit(10 ** 6)
INF = 987654321  # 무한
N = int(input())
cache = [INF] * (N + 1)
cache[1] = 0


def dp(x):
    if cache[x] != INF:
        return cache[x]

    if x % 6 == 0:
        cache[x] = min(dp(x // 3), dp(x // 2)) + 1
    elif x % 3 == 0:
        cache[x] = min(dp(x // 3), dp(x - 1)) + 1
    elif x % 2 == 0:
        cache[x] = min(dp(x // 2), dp(x - 1)) + 1
    else:
        cache[x] = dp(x - 1) + 1

    return cache[x]


print(dp(N))
