#-*- coding: utf-8 -*-

#11651 좌표 정렬하기 2.py

import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in sorted(lst, key = lambda x: (x[1], x[0])):
    print('{} {}'.format(i[0],i[1]))