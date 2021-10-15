N = int(input())
val = []
stk = []
s = input()
for _ in range(N):
    val.append(int(input()))

for ch in s:
    if ch.isalpha():
        stk.append(val[ord(ch) - ord('A')])
    else:
        b = stk.pop()
        a = stk.pop()
        if ch == '+':
            stk.append(a + b)
        elif ch == '-':
            stk.append(a - b)
        elif ch == '*':
            stk.append(a * b)
        else:
            stk.append(a / b)

print(f'{stk[0]:.2f}')
