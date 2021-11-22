N = int(input())
A = list(map(int, input().split()))
B = sorted([(val, i) for i, val in enumerate(A)])
P = [-1] * N
for i, pair in enumerate(B):
    P[pair[1]] = i

print(" ".join(map(str, P)))
