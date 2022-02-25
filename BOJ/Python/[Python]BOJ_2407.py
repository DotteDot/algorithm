#-*- coding: utf-8 -*-

#2407 조합.py

a, b = map(int, input().split())
c, d = 1, 1
for i in range(b):
    c *= a-i
    d *= i+1
print(c//d)