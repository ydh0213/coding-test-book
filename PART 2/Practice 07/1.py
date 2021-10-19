N, M = map(int, input().split())
lessons = list(map(int, input().split()))
l = max(lessons)
r = sum(lessons)
m = (l + r) // 2
ans = r


def is_possible(sz):
    cnt = 1
    bluray = 0
    for lesson in lessons:
        if bluray + lesson <= sz:
            bluray += lesson
        else:
            cnt += 1
            bluray = lesson

    return cnt <= M


while l <= r:
    if is_possible(m):
        ans = m
        r = m - 1
    else:
        l = m + 1

    m = (l + r) // 2

print(ans)
