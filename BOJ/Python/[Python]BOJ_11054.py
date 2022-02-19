#-*- coding: utf-8 -*-

#11054 가장 긴 바이토닉 부분 수열.py

import sys

def search_front(lst):
    n = len(lst)
    tmp = [0]*n
    tmp[0] = 1
    for s in range(1, n):
        smax, sidx = 0, -1
        for e in range(s)[::-1]:
            if lst[s] > lst[e]:
                if smax < tmp[e]:
                    smax = tmp[e]
                    sidx = e
                elif smax == tmp[e]:
                    if lst[e] < lst[sidx]:
                        smax = tmp[e]
                        sidx = e
        tmp[s] = tmp[sidx]+1
    return tmp


if __name__=="__main__":
    input = sys.stdin.readline
    n = int(input())
    seq = list(map(int, input().split()))
    if n == 1: print(1); exit()
    MAX = 0

    f = search_front(seq)
    b = search_front(list(reversed(seq)))
    for i in range(n):
        MAX = max(f[i]+b[-i-1]-1, MAX)
    print(MAX)