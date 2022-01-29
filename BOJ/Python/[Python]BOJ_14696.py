#-*- coding: utf-8 -*-

#14696 딱지놀이.py

import sys

input = sys.stdin.readline
N = int(input())

# 4: ★, 3: ●, 2: ■, 1: ▲
for _ in range(N):
    A = { '4':0, '3':0, '2':0, '1':0 }
    B = { '4':0, '3':0, '2':0, '1':0 }
    win = ''

    for i in list(input().split())[1:]: A[i] += 1
    for i in list(input().split())[1:]: B[i] += 1

    if A['4'] > B['4']: win = 'A'
    elif A['4'] < B['4']: win = 'B'
    elif A['3'] > B['3']: win = 'A'
    elif A['3'] < B['3']: win = 'B'
    elif A['2'] > B['2']: win = 'A'
    elif A['2'] < B['2']: win = 'B'
    elif A['1'] > B['1']: win = 'A'
    elif A['1'] < B['1']: win = 'B'
    else: win = 'D'

    print(win)