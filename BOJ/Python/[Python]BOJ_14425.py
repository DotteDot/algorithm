#-*- coding: utf-8 -*-

#14425 문자열 집합.py

n, m = map(int, input().split())
dictionary = dict.fromkeys(range(500),[])

for _ in range(n):
    h = hash(input())
    idx = h % 500
    dictionary[idx].append(h)


cnt = 0
for _ in range(m):
    h = hash(input())
    if h in dictionary[h%500]:
        cnt += 1
print(cnt)