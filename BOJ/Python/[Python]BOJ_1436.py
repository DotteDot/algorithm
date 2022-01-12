def check(n):
    cnt = 0
    for i in str(n):
        if i == '6':
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return 1
    return 0

n = int(input())

cnt = 0
for i in range(666,10000000):
    if check(i) == 1:
        cnt += 1
        if cnt == n:
            print(i)
            break