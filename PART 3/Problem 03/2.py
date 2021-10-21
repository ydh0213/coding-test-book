from itertools import combinations

N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


ans = 2 * N * len(houses)
for combi in combinations(chickens, M):
    tot = 0
    for house in houses:
        tot += min(get_dist(house, chicken) for chicken in combi)

    ans = min(ans, tot)

print(ans)
