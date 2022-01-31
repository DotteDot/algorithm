#-*- coding: utf-8 -*-

#10163 색종이.py

import sys

input = sys.stdin.readline
matrix = [[0]*1001 for _ in range(1001)]
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
paper_dict = {i:0 for i in range(1, N+1)}

for idx, p in enumerate(paper):
    sx, sy, x, y = p
    for i in range(y):
        for j in range(x):
            matrix[sy+i][sx+j] = idx+1

for i in range(1001):
    for j in matrix[i]:
        if j: paper_dict[j] += 1

for i in range(1, N+1):
    print(paper_dict[i])