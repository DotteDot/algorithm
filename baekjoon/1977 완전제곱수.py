import sys
input = sys.stdin.readline

a, b = int(input()), int(input())
result = []
for i in range(1000):
    if i * i <= b and i * i >= a:
        result.append(i*i)
    if i * i > b:
        break
if not result:
    print(-1)
else:
    print(sum(result))
    print(min(result))