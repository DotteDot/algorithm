#-*- coding: utf-8 -*-

#1193.py

n = int(input())

lst = [1]
num = 1
for i in range(1,4500):
    num += i
    lst.append(num)

idx = 0
for i in range(4500):
    if lst[i] <= n < lst[i+1]:
        idx = i

# print(lst[:6])
f_sum = idx + 2
a,b = n-lst[idx]+1, f_sum-(n-lst[idx]+1)
if f_sum%2 == 0:
    print('{}/{}'.format(b,a))
else:
    print('{}/{}'.format(a,b))