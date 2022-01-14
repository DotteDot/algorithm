#-*- coding: utf-8 -*-

#1181 단어 정렬.py

import sys

input = sys.stdin.readline
n = int(input())
lst = [[] for _ in range(51)]

for _ in range(n):
    word = input().strip()
    word_len = len(word)

    if word not in lst[word_len]:
        lst[word_len].append(word)
        lst[word_len].sort()

for i in lst:
    if i:
        for j in i: print(j)