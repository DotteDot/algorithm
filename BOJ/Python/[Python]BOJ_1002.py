#-*- coding: utf-8 -*-

#1002.py

'''
1. 딱 중간이면 1
2. 중간보다 겹치면 2
3. 안겹치면 0
4. 두명의 위치가 같으면 -1 (무한)
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if dist == 0 and r1 == r2: print(-1)
    elif dist == r1+r2 or abs(r1-r2) == dist: print(1)
    elif abs(r1-r2) < dist < r1+r2: print(2)
    else: print(0)