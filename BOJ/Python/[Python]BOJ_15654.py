#-*- coding: utf-8 -*-

#15654 N과 M (5).py

m, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

def permutation():
    if len(result) == n:
        print(' '.join(map(str, result)))
        return

    for i in lst:
        if i not in result:
            result.append(i)
            permutation()
            result.pop()

permutation()