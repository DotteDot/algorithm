#-*- coding: utf-8 -*-

#15656 N과 M (7).py

m, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

def BF():
    if len(result) == n:
        print(' '.join(map(str, result)))
        return

    for i in range(m):
        result.append(lst[i])
        BF()
        result.pop()

BF()