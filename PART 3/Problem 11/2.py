N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
chk = [False] * N
P = []
for i in A:
    for j in range(B.index(i), N):
        if i == B[j] and not chk[j]:
            chk[j] = True
            P.append(j)
            break

print(" ".join(map(str, P)))
