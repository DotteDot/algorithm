#-*- coding: utf-8 -*-

#1427 소트인사이드.py

import sys

input = sys.stdin.readline

a = list(input().strip())
a = sorted(a, reverse = True)

print(''.join(a))