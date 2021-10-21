tc = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break

    print(f'Case {tc}: {V // P * L + min(V % P, L)}')

    tc += 1
