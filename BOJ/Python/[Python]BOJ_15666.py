#-*- coding: utf-8 -*-

#15666 N과 M (12).py

m, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

def combination(s):
    if len(result) == n:
        print(' '.join(map(str, result)))
    
    else:
        before = None
        
        for i in range(s, m):
            if before == lst[i]: continue
            result.append(lst[i])
            combination(i)
            before = result.pop()

combination(0)