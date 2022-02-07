#-*- coding: utf-8 -*-

#1904 01타일.py

n = int(input())
arr = [1, 2]

for i in range(2, n):
    arr.append((arr[i - 1] + arr[i - 2]) % 15746)

print(arr[n-1])