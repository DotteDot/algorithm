#-*- coding: utf-8 -*-

#14501 퇴사.py

mat = [0]*31
n = int(input())

for i in range(1,n+1):
    t, p = map(int, input().split())
    mat[i+t] = max(mat[i+t], max(mat[:i+1])+p)
print(max(mat[:n+2]))