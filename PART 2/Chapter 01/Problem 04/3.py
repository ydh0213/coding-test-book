import sys, heapq

input = sys.stdin.readline
min_heap = []  # 양수
max_heap = []  # 음수
for _ in range(int(input())):
    x = int(input())
    if x > 0:
        heapq.heappush(min_heap, x)
    elif x < 0:
        heapq.heappush(max_heap, -x)
    else:
        if len(min_heap):
            if len(max_heap) == 0 or min_heap[0] < max_heap[0]:
                print(heapq.heappop(min_heap))
            else:
                print(-heapq.heappop(max_heap))
        else:
            print(-heapq.heappop(max_heap) if len(max_heap) else 0)
