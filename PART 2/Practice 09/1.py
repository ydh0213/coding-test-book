N = int(input())
A = list(map(int, input().split()))
cache = [0] * N
cache[0] = A[0]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            cache[i] = max(cache[i], cache[j])

    cache[i] += A[i]

print(max(cache))
