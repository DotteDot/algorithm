import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    if lst.count(0) == 3:
        break
    l = max(lst)
    del lst[lst.index(l)]
    a = 0

    for i in lst:
        a += i**2

    if a == l**2: print('right')
    else: print('wrong')