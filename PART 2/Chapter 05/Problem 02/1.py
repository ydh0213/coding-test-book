from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
ans = []
for i in map(int, input().split()):
    ans.append(bisect_right(cards, i) - bisect_left(cards, i))

print(' '.join(map(str, ans)))
