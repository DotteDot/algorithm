#-*- coding: utf-8 -*-

#1100 하얀 칸.py

chess = [list(input().strip()) for _ in range(8)]

cnt = 0
for i in range(8):
    if i % 2:
        for j in chess[i][1::2]:
            if j == 'F': cnt += 1
    else:
        for j in chess[i][::2]:
            if j == 'F': cnt += 1
print(cnt)