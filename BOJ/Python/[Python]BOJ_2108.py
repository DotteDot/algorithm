#-*- coding: utf-8 -*-

#2108 통계학.py
 
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())

lst = sorted([int(input()) for _ in range(N)])
a, b, c, d = round(sum(lst) / N), lst[N//2], lst[0], lst[-1] - lst[0]

count = Counter(lst).most_common(2)
if N != 1: c = count[1][0] if count[0][1] == count[1][1] else count[0][0]

print(f'{a}\n{b}\n{c}\n{d}')