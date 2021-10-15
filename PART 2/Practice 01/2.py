from collections import deque

for _ in range(int(input())):
    dq1 = deque()  # 커서 왼쪽
    dq2 = deque()  # 커서 오른쪽
    for ch in input():
        if ch == '<':
            if len(dq1) > 0:
                dq2.appendleft(dq1.pop())
        elif ch == '>':
            if len(dq2) > 0:
                dq1.append(dq2.popleft())
        elif ch == '-':
            if len(dq1) > 0:
                dq1.pop()
        else:
            dq1.append(ch)

    print(''.join(dq1) + ''.join(dq2))
