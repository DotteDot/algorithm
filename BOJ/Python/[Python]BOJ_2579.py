#-*- coding: utf-8 -*-

#2579 계단오르기.py

import sys

input = sys.stdin.readline
N = int(input())
stairs = [int(input()) for _ in range(N)]
if N == 1:print(stairs[0]);exit()
arr = [[]]*(N+1)
arr[0] = [stairs[0], 0]
arr[1] = [stairs[1], stairs[1] + arr[0][0]]

for i in range(2, N):
    arr[i] = [stairs[i] + max(arr[i-2]), stairs[i] + arr[i-1][0]]

print(max(arr[N-1]))