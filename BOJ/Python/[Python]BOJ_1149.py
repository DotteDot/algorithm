#-*- coding: utf-8 -*-

#1149 RGB거리.py

import sys

input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    matrix[i][0] += min(matrix[i-1][1], matrix[i-1][2])
    matrix[i][1] += min(matrix[i-1][0], matrix[i-1][2])
    matrix[i][2] += min(matrix[i-1][0], matrix[i-1][1])

print(min(matrix[-1]))