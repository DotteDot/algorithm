#-*- coding: utf-8 -*-

#13300 방 배정.py

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
female = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
male = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
lst = female, male
cnt = 0

for _ in range(N):
    S, Y = map(int, input().split())

    if S == 0: female[Y] += 1
    else: male[Y] += 1

for sex in lst:
    for stu in sex.values():
        if stu % K: cnt += stu // K + 1
        else: cnt += stu // K

print(cnt)