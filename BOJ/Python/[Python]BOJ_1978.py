import sys
input = sys.stdin.readline

_ = input()
a = list(map(int, input().split()))
if 1 in a:
    del a[a.index(1)]
cnt = 0
for i in a:
    flag = 0
    for j in range(2,1001):
        if j>i:
            break
        if i % j == 0 and i != j:
            flag = 1
    if flag == 0:
        cnt += 1

print(cnt)