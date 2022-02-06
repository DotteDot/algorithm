#-*- coding: utf-8 -*-

#9461 파도반 수열.py

n = int(input())
for _ in range(n):
    lst = [1,1,1]
    target = int(input())

    if target > 2:
        for i in range(3, target + 1):
            lst.append(lst[i - 3] + lst[i - 2])

    print(lst[target - 1])