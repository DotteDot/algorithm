#-*- coding: utf-8 -*-

#10814 나이순 정렬.py

import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    x, y = input().split()
    lst.append([int(x), y])

for i in sorted(lst, key = lambda x:x[0]):
    print(f'{i[0]} {i[1]}')