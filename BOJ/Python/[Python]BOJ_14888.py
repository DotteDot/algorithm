#-*- coding: utf-8 -*-

#14888 연산자 끼워넣기.py

# 순열을 사용하지 않고 모든 경우를 다 찾아보는 방법
# 백트래킹도 아니고, 순열도 쓰지않은 모든 경우를 다 찾는 방법
# 찐 브루트포스

'''import sys

# 모든 경우의 수 : 11! = 약 4천만 
# 시간제한 : 2초
# => brute force 가능??

#1 받아오기
global MAX, MIN

MAX, MIN = -1000000000, 1000000000
input = sys.stdin.readline
N = int(input())
numbers = list(input().split())[::-1]       # 앞쪽부터 다뤄줘야하기 때문에
symbols = list(map(int, input().split()))   # 스택처럼 pop, append를 쉽게 하려고 역순으로 나열
sym_list, check = [], [False] * (N - 1)

for i, j in enumerate(symbols):
    if i == 0:
        sym_list.extend(['+'] * j)
    if i == 1:
        sym_list.extend(['-'] * j)
    if i == 2:
        sym_list.extend(['*'] * j)
    if i == 3:
        sym_list.extend(['//'] * j)

#2 값 구하기
def calculate(number_lst, check_lst, result):
    global MAX, MIN

    if not number_lst:
        MAX, MIN = max(MAX, result), min(MIN, result)
        return 
    else:
        x = result
        y = number_lst.pop()

        for i in range(N - 1):
            if check_lst[i] == False:
                check_lst[i] = True

                if int(x) < 0 and sym_list[i] == '//':
                    calculate(number_lst, check_lst, -eval(f'{-int(x)}{sym_list[i]}{y}'))
                else:
                    calculate(number_lst, check_lst, eval(f'{x}{sym_list[i]}{y}'))

                check_lst[i] = False
        number_lst.append(y)

calculate(numbers, check, numbers.pop())
print(MAX)
print(MIN)'''

#-*- coding: utf-8 -*-

#14888 연산자 끼워넣기.py

# 순열을 사용해 모든 경우를 본다
# 백트래킹으로 풀지 않음.!!!

import sys
from itertools import permutations
# 모든 경우의 수 : 11! = 약 4천만 
# 시간제한 : 2초
# => brute force 가능??

#1 받아오기
global MAX, MIN

MAX, MIN = -1000000000, 1000000000
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
symbols = list(map(int, input().split()))
sym_list, check = [], [False] * (N - 1)

for i, j in enumerate(symbols):
    if i == 0:
        sym_list.extend(['+'] * j)
    if i == 1:
        sym_list.extend(['-'] * j)
    if i == 2:
        sym_list.extend(['*'] * j)
    if i == 3:
        sym_list.extend(['//'] * j)

sym_list = permutations(sym_list, N - 1)

#2 값 구하기
def calculate():
    global MAX, MIN

    for symbol in sym_list:
        result = numbers[0]
        
        for j in range(N - 1):
            if symbol[j] == '+':
                result += numbers[j+1]
            elif symbol[j] == '-':
                result -= numbers[j+1]
            elif symbol[j] == '*':
                result *= numbers[j+1]
            else:
                result = int(result / numbers[j+1])
    
        MAX, MIN = max(MAX, result), min(MIN, result)
    
calculate()
print(MAX)
print(MIN)