N = int(input())
cards = {}
for i in map(int, input().split()):
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1

M = int(input())
ans = []
for i in map(int, input().split()):
    ans.append(cards[i] if i in cards else 0)

print(' '.join(map(str, ans)))
