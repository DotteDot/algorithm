#-*- coding: utf-8 -*-

#3036 링.py

import sys
input = sys.stdin.readline

def gcd(x, y):
    if x%y != 0:
        return gcd(y, x%y)
    else:
        return y

_ = input()
a = list(map(int, input().split()))
a, lst = a[0], a[1:]

for i in lst:
    g = gcd(a, i)
    print('{}/{}'.format(a//g, i//g))