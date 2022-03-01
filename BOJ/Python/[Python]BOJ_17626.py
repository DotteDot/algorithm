#-*- coding: utf-8 -*-

#17626 Four Squares.py

N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp[N])


# def dfs(idx, n, s):
#     global MIN
#     if s == n:
#         MIN = min(MIN, len(use))
#         # print(use)
#         return

#     for i in range(idx, 225):
#         if lst[i]+s <= n and len(use) < MIN-1:
#             use.append(lst[i])
#             dfs(i, n, lst[i]+s)
#             use.pop()

# global MIN
# MIN = 50000
# lst = [i*i for i in range(225)[::-1]]
# use = []

# dfs(0, int(input()), 0)
# print(MIN)

# n = int(input())
# lst = [0]*(n+1)

# for i in range(1,n+1):
#     if i**(1/2) == int(i**(1/2)):
#         lst[i] = 1
#     else:
#         if i%2:
#             ipt = i//2+1
#         else:
#             ipt = i//2
#         tmp = 5
#         for j in range(1,ipt+1):
#             tmp = min(tmp, lst[j]+lst[i-j])
#         lst[i] = tmp
# print(lst[n])