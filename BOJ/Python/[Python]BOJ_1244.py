#-*- coding: utf-8 -*-

#1244 스위치 켜고 끄기.py

import sys

input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    xy, number = map(int, input().split())

    if xy == 1:
        num = number - 1

        while num <= n - 1:
            switch[num] = (switch[num] + 1) % 2
            num += number
    
    else:
        front = back = number - 1
        switch[back] = (switch[back] + 1) % 2
        
        while True:
            front -= 1
            back += 1

            if front < 0 or back > n - 1:
                break

            if switch[front] == switch[back]:
                switch[front] = switch[back] = (switch[back] + 1) % 2

            else:
                break


div = n // 20
side = n % 20
for i in range(div):
    print(' '.join(map(str, switch[i * 20:i * 20 + 20])))
print(' '.join(map(str, switch[(n // 20) * 20:])))
