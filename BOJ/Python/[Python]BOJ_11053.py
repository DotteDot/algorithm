#-*- coding: utf-8 -*-

#11053 가장 긴 증가하는 부분 수열.py

import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
mat = [0] * (n+1)
mat[0] = 1

# s_max : 제일 긴 수열의 길이
# s_idx : 제일 긴 수열의 index
for s in range(1, n):
    s_max, s_idx = 0, n
    for e in reversed(range(s)):
        # start 위치의 숫자보다 작은 숫자를 찾는다
        if lst[e] < lst[s]:
            # 제일 긴 수열보다 긴 수열이라면 바꿔준다
            if s_max < mat[e]:
                s_max = mat[e]
                s_idx = e
            # 제일 긴 수열과 길이가 같을 때
            elif s_max == mat[e]:
                # 제일 긴 수열이라고 저장되어있는
                # 위치의 숫자보다 작은 숫자면 바꿔준다
                if lst[e] <  lst[s_idx]:
                    s_max = mat[e]
                    s_idx = e
    mat[s] = mat[s_idx] + 1

print(max(mat))