#-*- coding: utf-8 -*-

#2116 주사위 쌓기.py

import sys

def get_max(a, b):
    floor = [a, b]                                  # 주사위 천장과 바닥
    
    if min(floor) == 5: return 4                    # [6, 5]
    elif max(floor) == 6: return 5                  # [6, i]
    else: return 6                                  # [6제외]


input = sys.stdin.readline
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
num_set = [5, 3, 4, 1, 2, 0]
result = [0] * 6

for f in range(6):
    un, up = f, num_set[f]
    next_under = dice[0][up]
    result[f] += get_max(dice[0][un], dice[0][up])
    
    for i in range(1, N):
        un = dice[i].index(next_under)
        up = num_set[un]
        next_under = dice[i][up]
        result[f] += get_max(dice[i][un], dice[i][up])

print(max(result))