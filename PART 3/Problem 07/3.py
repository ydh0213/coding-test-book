from collections import deque

N = int(input())
nums = list(map(int, input().split()))
ops_cnt = list(map(int, input().split()))
ans_max = -1_000_000_001
ans_min = 1_000_000_001
dq = deque()
dq.append((nums[0], 1, ops_cnt[0], ops_cnt[1], ops_cnt[2], ops_cnt[3]))
while dq:
    res, n, plus, minus, multi, div = dq.popleft()
    if n == N:
        ans_max = max(ans_max, res)
        ans_min = min(ans_min, res)
        continue

    if plus:
        dq.append((res + nums[n], n + 1, plus - 1, minus, multi, div))

    if minus:
        dq.append((res - nums[n], n + 1, plus, minus - 1, multi, div))

    if multi:
        dq.append((res * nums[n], n + 1, plus, minus, multi - 1, div))

    if div:
        next_res = res // nums[n] if res >= 0 else -(-res // nums[n])
        dq.append((next_res, n + 1, plus, minus, multi, div - 1))

print(ans_max)
print(ans_min)
