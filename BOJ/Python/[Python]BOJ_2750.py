#-*- coding: utf-8 -*-

#2750 수 정렬하기.py


import sys

input = sys.stdin.readline
n = int(input())
not_sort = [int(input()) for _ in range(n)]

# Selection Sort
# 코드를 다 보고 제일 작은것을 앞으로 뺀다.
# 앞으로 빠진것 제외하고 제일 작은것을 선택해 앞으로 뺀다.
check = [False]*n
result = []
for _ in range(n):
    pin = 0
    for i in range(n):
        
        if check[i] == False and not_sort[i] < not_sort[pin]:
            # print(i, pin, not_sort[i], not_sort[pin])
            pin = i
    # print(pin, check)
    print(not_sort[pin])
    # result.append(not_sort[pin])
    check[pin] = True
# print(result)

# 업데이트 할 예정
