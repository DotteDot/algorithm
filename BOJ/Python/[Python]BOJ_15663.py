#-*- coding: utf-8 -*-

#15663 N과 M (9).py

m, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []
tmp = []

def permutation():
    if len(result) == n:
        print(' '.join(map(str, result)))
    
    else:
        before = None
        for i in range(m):
            if before == lst[i] or i in tmp: continue
            result.append(lst[i])
            tmp.append(i)
            permutation()
            before = result.pop()
            tmp.pop()

permutation()