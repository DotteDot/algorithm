#-*- coding: utf-8 -*-

#1912 연속합.py

import sys

input = sys.stdin.readline
input()
mat = list(map(int, input().split()))
s = mx = mat[0]

for i in mat[1:]:
    mx = max(mx, s)
    s = i if s+i <= 0 or s+i < i else s + i
mx = max(mx, s)
print(mx)