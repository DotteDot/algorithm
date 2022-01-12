n = int(input())
a, b = '*', ' *'
for _ in range(n-1):a += ' *';b += ' *'

flag = 0
for _ in range(n):
    if flag == 0:print(a);flag=1
    else:print(b);flag=0