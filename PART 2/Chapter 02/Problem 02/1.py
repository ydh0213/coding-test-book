T = [n * (n + 1) // 2 for n in range(46)]


def is_possible(K):
    for i in range(1, 46):
        for j in range(i, 46):
            for k in range(j, 46):
                if T[i] + T[j] + T[k] == K:
                    return 1

    return 0


for _ in range(int(input())):
    print(is_possible(int(input())))
