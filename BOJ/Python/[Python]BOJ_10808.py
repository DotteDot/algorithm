#-*- coding: utf-8 -*-

#10808 알파벳 개수.py

matrix = [0]*26
for i in input():
    matrix[ord(i)-97] += 1

print(' '.join(map(str, matrix)))