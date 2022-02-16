#-*- coding: utf-8 -*-

#10844 쉬운 계단 수.py

n = int(input())
lst = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    (
        lst[0],lst[1],lst[2],lst[3],lst[4],
        lst[5],lst[6],lst[7],lst[8],lst[9]
    ) = (
            lst[1],lst[0]+lst[2],lst[1]+lst[3],lst[2]+lst[4],lst[3]+lst[5],
            lst[4]+lst[6],lst[5]+lst[7],lst[6]+lst[8],lst[7]+lst[9],lst[8]
        )

print(sum(lst)%1000000000)