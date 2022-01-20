#-*- coding: utf-8 -*-

#1759 암호 만들기.py

from sys import stdin
from itertools import combinations

input = stdin.readline

n, _ = map(int, input().split())
lst = sorted(list(input().split()))

for i in combinations(lst, n):
    aeiou = i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u')
    el = n - aeiou

    if aeiou >= 1 and el >= 2:
        print(''.join(i))