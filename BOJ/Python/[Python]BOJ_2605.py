#-*- coding: utf-8 -*-

#2605 줄 세우기.py

N = int(input())
row = []

for i, j in enumerate(list(map(int, input().split()))):
    tmp = []

    if not row:
        row.append(i+1)
    else:
        for _ in range(j):
            tmp.append(row.pop(i-j))
        row.append(i+1)
        row.extend(tmp)
        
print(' '.join(map(str, row)))