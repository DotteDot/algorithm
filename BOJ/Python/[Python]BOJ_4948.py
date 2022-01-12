#-*- coding: utf-8 -*-

#4948 베르트랑 공준.py

import sys
input = sys.stdin.readline
prime = [True]*(246913)

for i in range(2, 246913):
    if prime[i] == True:
        for j in range(i+i,246913,i):
            # print(j)
            prime[j] = False
# print(prime[13:27])
while True:
    n = int(input())
    if n == 0: break

    print(prime[n+1:2*n+1].count(True))