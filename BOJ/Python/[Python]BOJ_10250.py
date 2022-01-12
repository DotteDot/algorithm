#-*- coding: utf-8 -*-

#10250 ACM 호텔.py

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n%h == 0:
        print(h*100+ n//h)
    else:
        print(n%h*100+ n//h+1)