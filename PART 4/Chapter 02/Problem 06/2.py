from collections import Counter
from itertools import combinations


def solution(orders, course):
    ans = []
    for n in course:
        menus = []
        for order in orders:
            menus += combinations(sorted(order), n)

        res = Counter(menus).most_common()
        for menu, cnt in res:
            if cnt >= 2:
                ans.append(''.join(menu))

    return sorted(ans)