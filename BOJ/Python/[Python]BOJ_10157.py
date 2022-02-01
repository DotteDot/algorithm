#-*- coding: utf-8 -*-

#10157 자리배정.py

x, y = map(int, input().split())
K = int(input())
nx, ny = x, y
s = 0
cnt = 0

if x * y < K:
    print(0)
else:
    for i in range(x // 2 + 1):
        if s < K <= s + 2 * ( x + y - 2 ):
            break
        s += 2 * ( x + y - 2 )
        x -= 2
        y -= 2
        cnt += 1

    if s < K <= s + y - 1:
        print(cnt + 1, cnt + K - s)
    elif s + y - 1 < K <= s + y + x - 2:
        print(cnt + K - s - y + 1, cnt + y )
    elif s + y + x - 2 < K <= s + 2 * y + x - 3:
        print(cnt + x, ny - cnt - (K - s - y - x + 1))
    elif s + 2 * y + x - 3 < K:
        print(nx - cnt - (K - s - 2 * y - x + 2), cnt + 1)
