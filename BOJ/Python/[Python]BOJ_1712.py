#-*- coding: utf-8 -*-

#1712 손익분기점.py

import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

n = 0
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)