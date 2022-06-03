#-*- coding: utf-8 -*-

#2512 예산.py

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())

mid = 0
s,e = 1, max(lst)
result = 0
while s <= e:
    print(f'm:{m}, s:{s}, e:{e}')
    mid = (e+s)//2
    
    tmp = 0
    for i in lst:
        if i > mid:
            tmp += mid
        else:
            tmp += i
    
    print(f'mid:{mid}, tmp:{tmp}')
    print()
    if tmp > m:
        e = mid-1
    else:
        result = mid
        s = mid+1

print(result)