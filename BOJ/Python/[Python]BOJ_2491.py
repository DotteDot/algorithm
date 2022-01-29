#-*- coding: utf-8 -*-

#2491 수열.py

import sys

input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))
lst = [range(0, N), reversed(range(0, N))]
max_len = 0

for loop in lst:
    tmp = []

    for i in loop:
        if not tmp or tmp[-1] <= seq[i]:
            tmp.append(seq[i])

        else:
            max_len = max(max_len, len(tmp))
            tmp = [seq[i]]

    max_len = max(max_len, len(tmp))

print(max_len)