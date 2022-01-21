#-*- coding: utf-8 -*-

#15655 N과 M (6).py

m, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

def combination(num):
    if len(result) == n:
        print(' '.join(map(str, result)))
        return

    for i in range(num, m):
        if lst[i] not in result:
            result.append(lst[i])
            combination(i)
            result.pop()

combination(0)