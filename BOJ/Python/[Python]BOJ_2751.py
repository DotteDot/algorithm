#-*- coding: utf-8 -*-

#2751 수 정렬하기 2.py

import sys
input = sys.stdin.readline
for i in sorted([int(input()) for _ in range(int(input()))]):
    print(i)