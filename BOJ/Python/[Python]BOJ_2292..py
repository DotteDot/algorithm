#-*- coding: utf-8 -*-

#2292 벌집.py

n = int(input())

cnt = 1
mx, mn = 7, 1
if n == 1:
    print(1)
else:
    while True:
        if mn < n <= mx:
            print(cnt+1)
            break
        else:
            cnt += 1
            mx, mn = mx + 6*cnt, mx