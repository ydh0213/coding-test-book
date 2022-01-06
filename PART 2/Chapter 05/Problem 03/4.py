from collections import deque

N = int(input())
dq = deque()
dq.append((N, 0))
chk = [False] * (N + 1)
chk[N] = True

while dq:
    X, d = dq.popleft()
    if X == 1:
        print(d)
        break

    if X % 3 == 0 and not chk[X // 3]:
        dq.append((X // 3, d + 1))
        chk[X // 3] = True

    if X % 2 == 0 and not chk[X // 2]:
        dq.append((X // 2, d + 1))
        chk[X // 2] = True

    if not chk[X - 1]:
        dq.append((X - 1, d + 1))
        chk[X - 1] = True
