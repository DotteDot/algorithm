#-*- coding: utf-8 -*-

#1085.py

x, y, w, h = map(int, input().split())

mn = 1000
mn = min(mn, x)
mn = min(mn, y)
mn = min(mn, w-x)
mn = min(mn, h-y)
print(mn)