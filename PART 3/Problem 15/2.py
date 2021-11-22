N = int(input())
dice = list(map(int, input().split()))


def get_min3():
    res = 150
    for i in range(4):
        for j in range(i + 1, 5):
            if i + j != 5:
                for k in range(j + 1, 6):
                    if j + k != 5 and k + i != 5:
                        res = min(res, dice[i] + dice[j] + dice[k])

    return res


def get_min2():
    res = 100
    for i in range(5):
        for j in range(i + 1, 6):
            if i + j != 5:
                res = min(res, dice[i] + dice[j])

    return res


if N == 1:
    print(sum(dice) - max(dice))
else:
    print(4 * get_min3() + 4 * (2 * N - 3) * get_min2() + (N - 2) * (5 * N - 6) * min(dice))
