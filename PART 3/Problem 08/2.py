from collections import Counter

alphabet_cnt = Counter(input())
if sum(cnt % 2 for cnt in alphabet_cnt.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''
    for ch, cnt in sorted(alphabet_cnt.items()):
        half += ch * (cnt // 2)

    ans = half
    for ch, cnt in alphabet_cnt.items():
        if cnt % 2:
            ans += ch
            break

    ans += ''.join(reversed(half))
    print(ans)
