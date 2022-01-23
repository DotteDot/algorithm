#-*- coding: utf-8 -*-

#2635 수 이어가기.py

n = int(input())

maximum, max_lst = 0, []
for i in reversed(range(n + 1)):
    lst = [n, i]
    
    while lst[-2] - lst[-1] >= 0:
        lst.append(lst[-2] - lst[-1])
    
    if maximum < len(lst):
        maximum = len(lst)
        max_lst = lst
        
print(maximum)
print(' '.join(map(str, max_lst)))