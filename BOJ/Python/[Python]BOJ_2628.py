#-*- coding: utf-8 -*-

#2628 종이자르기.py

import sys

input = sys.stdin.readline
x, y = map(int, input().split())
x_lst, y_lst = [False] * (x + 1), [False] * (y + 1)

for _ in range(int(input())):           # x, y List에 잘려지는 곳 저장
    a, b = map(int, input().split())

    if a == 0:
        y_lst[b] = True
    else:
        x_lst[b] = True

x_start = y_start = 0
x_max = y_max = 0

for i in range(1, x + 1):               # x의 최댓값
    if x_lst[i] == True or i == x:
        x_max = max(x_max, i - x_start)
        x_start = i

for i in range(1, y + 1):               # y의 최댓값
    if y_lst[i] == True or i == y:
        y_max = max(y_max, i - y_start)
        y_start = i

print(x_max * y_max)