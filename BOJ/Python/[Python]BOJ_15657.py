#-*- coding: utf-8 -*-

#15657 N과 M (8).py

m, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

def comb_repeat(num):
    if len(result) == n:
        print(' '.join(map(str, result)))
        return

    for i in range(num, m):
        result.append(lst[i])
        comb_repeat(i)
        result.pop()

comb_repeat(0)