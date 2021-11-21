from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
ops_cnt = []
for i, cnt in enumerate(map(int, input().split())):
    ops_cnt += [i] * cnt

ans_max = -1_000_000_001
ans_min = 1_000_000_001
for permu in set(permutations(ops_cnt, N - 1)):
    res = nums[0]
    for i, op in enumerate(permu):
        if op == 0:
            res += nums[i + 1]
        elif op == 1:
            res -= nums[i + 1]
        elif op == 2:
            res *= nums[i + 1]
        else:
            if res >= 0:
                res //= nums[i + 1]
            else:
                res = -(-res // nums[i + 1])

    if res > ans_max:
        ans_max = res

    if res < ans_min:
        ans_min = res

print(ans_max)
print(ans_min)
