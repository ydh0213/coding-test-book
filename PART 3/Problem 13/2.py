from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
ans = -1
for arr in set(permutations(A, N)):
    ans = max(ans, sum(abs(arr[i - 1] - arr[i]) for i in range(1, N)))

print(ans)
