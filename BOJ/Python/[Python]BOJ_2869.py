#-*- coding: utf-8 -*-

#2869 달팽이는 올라가고 싶다.py

import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

if (c-a)%(a-b) != 0: print((c-a)//(a-b)+2)
else: print((c-a)//(a-b)+1)