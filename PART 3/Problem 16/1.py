s = input()
N = len(s) if len(s) <= 9 else (len(s) - 9) // 2 + 9
chk = [False] * (N + 1)
is_found_ans = False


def backtracking(idx, arr):
    global is_found_ans
    if idx >= len(s):
        is_found_ans = True
        print(*arr)
        return

    n = int(s[idx])
    if n <= N and not chk[n]:
        chk[n] = True
        narr = arr[:]
        narr.append(n)
        backtracking(idx + 1, narr)
        if is_found_ans:
            return

        chk[n] = False

    if idx + 1 < len(s):
        n = int(s[idx:idx + 2])
        if n <= N and not chk[n]:
            chk[n] = True
            narr = arr[:]
            narr.append(n)
            backtracking(idx + 2, narr)
            if is_found_ans:
                return

            chk[n] = False


backtracking(0, [])
