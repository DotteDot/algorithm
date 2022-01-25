#-*- coding: utf-8 -*-

#15665 N과 M (11).py

m, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

def combination():
    if len(result) == n:
        print(' '.join(map(str, result)))
    
    else:
        before = None
        
        for i in range(m):
            if before == lst[i]: continue
            result.append(lst[i])
            combination()
            before = result.pop()

combination()