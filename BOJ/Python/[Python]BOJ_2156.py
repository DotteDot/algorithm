#-*- coding: utf-8 -*-

#2156 포도주 시식.py

arr = [[0,0,0],[0,0,0]]
for _ in range(int(input())):
    g = int(input())
    a = arr[-1][2] + g
    b = arr[-1][0] + g
    c = max(arr[-1])
    arr.append([a,b,c])
    
print(max(arr[-1]))