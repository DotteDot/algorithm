#-*- coding: utf-8 -*-

#10989 수 정렬하기 3.py

# print(10000000**0.5*10000000)
import sys
input = sys.stdin.readline

n = int(input())
lst = [0]*10001
for _ in range(n):
    num = int(input())
    lst[num] += 1

for i in range(1,10001):
    for j in range(lst[i]):
        print(i)