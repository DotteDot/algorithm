import sys
sys.setrecursionlimit(10**6)

lst = [0]*91
lst[1] = 1

for i in range(2,91):
    lst[i] = lst[i-1]+lst[i-2]

print(lst[int(input())])