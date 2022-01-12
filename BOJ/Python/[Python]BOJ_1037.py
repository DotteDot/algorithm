#-*- coding: utf-8 -*-

#1037.py

import sys

input = sys.stdin.readline

input()
lst = list(map(int, input().split()))
print(max(lst)*min(lst))