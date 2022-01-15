#-*- coding: utf-8 -*-

#11650 좌표 정렬하기.py

import sys

input = sys.stdin.readline
lst = [list(map(int, input().split())) for _ in range(int(input()))]
lst_sort = sorted(lst, key = lambda x: (x[0], x[1]))

for i in lst_sort: print(i[0], i[1])