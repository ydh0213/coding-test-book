def solution(N, stages):
    a = [0] * (N + 2)
    b = [0] * (N + 2)
    for stage in stages:
        a[stage] += 1
        b[stage] += 1

    for i in range(N, -1, -1):
        b[i] += b[i + 1]

    arr = [(a[i] / b[i] if b[i] else 0, i) for i in range(1, N + 1)]
    arr.sort(key=lambda x: (-x[0], x[1]))

    return [i[1] for i in arr]
