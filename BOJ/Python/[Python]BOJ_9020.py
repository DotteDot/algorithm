#-*- coding: utf-8 -*-

#9020 골드바흐의 추측.py

import sys
input = sys.stdin.readline
prime = [True]*10001

for i in range(2, 10001):
    if prime[i] == True:
        for j in range(i+i,10001,i):
            prime[j] = False

for _ in range(int(input())):
    n = int(input())
    for i in range(n//2,n+1):
        if prime[i] == True and prime[n-i] == True:
            print(n-i, i)
            break