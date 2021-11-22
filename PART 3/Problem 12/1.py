INF = 9876543210
cache = [INF] * 10_000_001  # 초기값: INF, 임시마크: 0
A, B, K = map(int, input().split())


def S(n):
    return sum(int(ch) ** K for ch in str(n))


def dfs(n):
    if cache[n] == INF:  # 최초 방문 노드
        cache[n] = 0  # 임시마크 해두고 탐색 시작
        cache[n] = min(n, dfs(S(n)))
    else:
        # 이미 탐색 완료한 노드라면 바로 반환
        if cache[n]:
            return cache[n]

        # 탐색 중인 노드 재방문. 즉, cycle 발견. 다시 cycle 돌면서 최솟값을 찾는다
        m = n
        nn = S(n)
        while nn != n:
            m = min(m, nn)
            nn = S(nn)

        # cycle 노드들에 최솟값을 갱신해준다
        cache[n] = m
        nn = S(n)
        while nn != n:
            cache[nn] = m
            nn = S(nn)

    return cache[n]


print(sum(dfs(i) for i in range(A, B + 1)))
