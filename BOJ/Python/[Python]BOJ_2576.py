import sys
input = sys.stdin.readline

s, m = 0, 700
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        s += num
        m = min(num, m)

if s == 0:
    print(-1)
else:
    print(s)
    print(m)