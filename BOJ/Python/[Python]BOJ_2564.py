#-*- coding: utf-8 -*-

#2564 경비원.py

import sys

input = sys.stdin.readline
x, y = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]
dong = list(map(int, input().split()))

# 1:북 2:남 3:서 4:동
# [0,4,3,1,2] 시계
# [0,3,4,2,1] 반시계
rotate_clock = [0,4,3,1,2]
back_clock = [0,3,4,2,1]


result = 0
for store in stores:
    if store[0] == dong[0]:
        result += abs(store[1] - dong[1])
    else:
        clock = store[0]
        clock_dist = 0
        if store[0] == 1:
            clock_dist += x - store[1]
        elif store[0] == 4:
            clock_dist += y - store[1]
        elif store[0] == 2:
            clock_dist += store[1]
        elif store[0] == 3:
            clock_dist += store[1]

        clock = rotate_clock[clock]
        while clock != dong[0]:
            if clock == 1 or clock == 2:
                clock_dist += x
            else:
                clock_dist += y
            clock = rotate_clock[clock]

        if dong[0] == 1:
            clock_dist += dong[1]
        elif dong[0] == 4:
            clock_dist += dong[1]
        elif dong[0] == 2:
            clock_dist += x - dong[1]
        elif dong[0] == 3:
            clock_dist += y - dong[1]

        back = store[0]
        back_dist = 0
        if store[0] == 1:
            back_dist += store[1]
        elif store[0] == 4:
            back_dist += store[1]
        elif store[0] == 2:
            back_dist += x - store[1]
        elif store[0] == 3:
            back_dist += y - store[1]

        back = back_clock[back]
        while back != dong[0]:
            if back == 1 or back == 2:
                back_dist += x
            else:
                back_dist += y
            back = back_clock[back]

        if dong[0] == 1:
            back_dist += x - dong[1]
        elif dong[0] == 4:
            back_dist += y - dong[1]
        elif dong[0] == 2:
            back_dist += dong[1]
        elif dong[0] == 3:
            back_dist += dong[1]
        
        result += min(back_dist, clock_dist)

print(result)