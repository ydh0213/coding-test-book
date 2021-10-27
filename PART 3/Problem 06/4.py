import heapq

for _ in range(int(input())):
    M = int(input())
    arr = []
    for _ in range(M // 10 + 1):
        for i in map(int, input().split()):
            arr.append(i)

    ans = []
    max_hq = []
    min_hq = []
    for i, val in enumerate(arr):
        if i % 2:
            heapq.heappush(min_hq, -heapq.heappushpop(max_hq, -val) if len(max_hq) and val < -max_hq[0] else val)
        else:
            heapq.heappush(max_hq, -heapq.heappushpop(min_hq, val) if len(min_hq) and val > min_hq[0] else -val)
            ans.append(-max_hq[0])

    print((M + 1) // 2)
    for i in range(len(ans) // 10 + 1):
        print(*ans[i * 10:(i + 1) * 10])
