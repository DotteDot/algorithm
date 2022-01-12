import sys
input = sys.stdin.readline
input()
a = list(map(int, input().split()))

b = 1
s = 0
for i in a:
    if i == 1:
        s += b
        b += 1
    else:
        b = 1
print(s)