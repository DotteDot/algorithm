import sys
input = sys.stdin.readline
n = int(input())
a = 1 - n
for _ in range(n):
    a += int(input())
print(a)