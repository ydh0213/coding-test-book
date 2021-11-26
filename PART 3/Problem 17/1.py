N, K = map(int, input().split())
schedule = list(map(int, input().split()))
ans = 0
multi_tap = []
for i, v in enumerate(schedule):
    if v in multi_tap:
        continue
    elif len(multi_tap) < N:
        multi_tap.append(v)
    else:
        ans += 1
        is_found = False
        nxt = (-1, 0)
        for j, val in enumerate(multi_tap):
            if val in schedule[i + 1:]:  # 가장 나중에 사용되는 전자기기를 찾아 갱신
                nxt_idx = schedule[i + 1:].index(val)
                if nxt[0] < nxt_idx:
                    nxt = (nxt_idx, j)
            else:  # 이후 사용되지 않는 전자기기가 있다면 그걸로 선택
                is_found = True
                multi_tap[j] = v
                break

        if not is_found:
            multi_tap[nxt[1]] = v

print(ans)
