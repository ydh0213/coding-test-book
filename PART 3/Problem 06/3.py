for _ in range(int(input())):
    M = int(input())
    ipt = []
    for _ in range(M // 10 + 1 if M % 10 else M // 10):
        ipt += map(int, input().split())

    arr = []
    ans = []
    for i, v in enumerate(ipt):
        arr.append(v)
        if (i & 1) == 0:
            arr.sort()
            ans.append(arr[i // 2])

    print(len(ans))
    for i in range(len(ans) // 10 + 1 if len(ans) % 10 else len(ans) // 10):
        print(*ans[i * 10:(i + 1) * 10])
