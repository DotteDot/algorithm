#-*- coding: utf-8 -*-

#18870 좌표 압축.py

import sys

input = sys.stdin.readline

_ = input()
lst = list(map(int, input().split()))
lst_sorted = sorted(list(set(lst)))

dic = {lst_sorted[i] : i for i in range(len(lst_sorted))}
for i in lst:
    print(dic[i], end=' ')