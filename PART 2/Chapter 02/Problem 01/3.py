h = [int(input()) for _ in range(9)]
tot = sum(h)


def solve():
    for i in range(8):
        for j in range(i + 1, 9):
            if tot - h[i] - h[j] == 100:
                for k in h:
                    if k != h[i] and k != h[j]:
                        print(k)

                return


solve()
