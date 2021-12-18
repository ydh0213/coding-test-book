import sys, heapq

input = sys.stdin.readline
hq = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heapq.heappop(hq)[1] if len(hq) else 0)
    else:
        heapq.heappush(hq, (abs(x), x))