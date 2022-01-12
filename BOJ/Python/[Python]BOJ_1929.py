#-*- coding: utf-8 -*-

#1929 소수 구하기.py

n, m = map(int, input().split())
prime = [True]*(m+1)

for i in range(2, m+1):
    if prime[i] == True:
        if n <= i <= m: print(i)
        for j in range(i,m+1,i):
            prime[j] = False